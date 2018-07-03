from flask import jsonify, request, Blueprint
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.Validate import FieldValidation
from app.Models import RideOffer, RideRequest
from app.db.db_functions import add_new_offer, get_user_by_username
import datetime

validate = FieldValidation()


class CreateOffer(MethodView):
    """ class for creating a new ride offer """

    @jwt_required
    def post(self):
        #get entered data
        offer_data = request.get_json()
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M")

        loggedin_user = get_jwt_identity()
        user = get_user_by_username(loggedin_user)

        driver_id = user[0]
        driver_name = user[1] +""+user[2]
        location = offer_data.get("location")
        car_type = offer_data.get("car_type")
        plate_number = offer_data.get("plate_number")
        contact = offer_data.get("contact")
        availability = offer_data.get("availability")
        cost_per_km = offer_data.get("cost_per_km")
        #validation
        response = validate.offer_validation(driver_name, location, car_type,
                                             plate_number, contact,
                                             availability, cost_per_km)
        if response:
            return jsonify(response), 400
       
        #storing entered request
        add_new_offer(
            driver_id = driver_id,
            date = date,
            driverName = driver_name,
            location=location,
            carType=car_type,
            plateNumber=plate_number,
            contact=contact,
            availability=availability,
            costPerKm=cost_per_km)

        new_offer = RideOffer(
            driver_name=driver_name,
            location=location,
            car_type=car_type,
            plate_number=plate_number,
            contact=contact,
            availability=availability,
            cost_per_km=cost_per_km)
        return jsonify({'Offer': new_offer.__dict__}), 200


class ViewAllOffers(MethodView):