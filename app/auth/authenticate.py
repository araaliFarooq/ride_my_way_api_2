from flask import request, jsonify, Blueprint
from flask.views import MethodView
from app.validate import FieldValidation
from app.db.db_functions import add_new_client, add_new_driver, get_user_by_username
from app.models import Driver, User
from flask_jwt_extended import create_access_token

validate = FieldValidation()
auth_blueprint = Blueprint("auth_blueprint", __name__)


class RegisterUser(MethodView):
    """ class to register a user """

    def post(self):
        """Create a new user"""
        reg_info = request.get_json()

        firstName = reg_info.get("firstName")
        secondName = reg_info.get("secondName")
        userName = reg_info.get("userName")
        contact = reg_info.get("contact")
        user_category = reg_info.get("user_category")
        password = reg_info.get("password")

        response = validate.client_validation(firstName, secondName, userName,
                                              contact, user_category, password)

        if response:
            return response

        if user_category == "driver":
            car_type = reg_info.get("car_type")
            reg_num = reg_info.get("reg_num")
            lic_num = reg_info.get("lic_num")

            response2 = validate.driver_validation(
                firstName, secondName, userName, contact, user_category,
                car_type, reg_num, lic_num, password)

            if response2:
                return response2
            # database function to add new driver
            add_new_driver(
                firstName=firstName,
                secondName=secondName,
                userName=userName,
                contact=contact,
                carType=car_type,
                reg_num=reg_num,
                lic_num=lic_num,
                password=password)
            # new driver object
            new_driver = Driver(
                firstName=firstName,
                secondName=secondName,
                userName=userName,
                contact=contact,
                user_category=user_category,
                car_type=car_type,
                reg_num=reg_num,
                lic_num=lic_num,
                password=password)
            return jsonify({"New Driver": new_driver.__dict__}), 200

        # database function to add new client
        add_new_client(
            firstName=firstName,
            secondName=secondName,
            userName=userName,
            contact=contact,
            password=password)
        new_client = User(
            firstName=firstName,
            secondName=secondName,
            userName=userName,
            contact=contact,
            user_category=user_category,
            password=password)
        return jsonify({"New Client": new_client.__dict__}), 200


class Login(MethodView):
    """ class to login a user """

    def post(self):
        """ user login """

        request_data = request.get_json()
        userName = request_data.get('userName')
        password = request_data.get('password')

        response = validate.login_validation(userName, password)

        if response:
            return response

        user_token = {}
        user = get_user_by_username(userName)

        if user:

            access_token = create_access_token(identity=userName)
            user_token["token"] = access_token
            return jsonify({"message": user_token}), 200

        return response


login_view = Login.as_view('login_view')
registry_view = RegisterUser.as_view('registery_view')

auth_blueprint.add_url_rule(
    '/api/v1/user/login', view_func=login_view, methods=['POST'])
auth_blueprint.add_url_rule(
    "/api/v1/user/register", view_func=registry_view, methods=['POST'])
