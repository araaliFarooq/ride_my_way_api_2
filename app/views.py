from flask import jsonify, request, Blueprint
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.Validate import FieldValidation
from app.Models import RideOffer, RideRequest
from app.db.db_functions import add_new_offer, get_user_by_username, get_all_ride_offers, get_rideoffer_details, get_requests_to_rideOffer, send_ride_request
import datetime

validate = FieldValidation()
ride_blueprint = Blueprint("ride_blueprint", __name__)


class CreateOffer(MethodView):
    """ class for creating a new ride offer """

    @jwt_required
    def post(self):
        #get entered data
        offer_data = request.get_json()
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M")

        loggedin_user = get_jwt_identity()
        user = get_user_by_username(username=loggedin_user)

        driver_id = user[0]
        driver_name = user[1] + "" + user[2]
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
            driver_id=driver_id,
            date=date,
            driverName=driver_name,
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
        return jsonify({'New Offer Added': new_offer.__dict__}), 200


class ViewAllOffers(MethodView):
    @jwt_required
    def get(self):
        """function to get all offers"""
        all_offers = get_all_ride_offers()
        return jsonify({"All Offers": all_offers})


class GetRideOfferDetails(MethodView):
    @jwt_required
    def get(self, ride_id):
        if len(ride_id) > 0 and ride_id != None:
            validation = validate.validate_entered_id(ride_id)
            if validation:
                return jsonify({"message": validation}), 400
            ride = get_rideoffer_details(ride_id=ride_id)
            return jsonify({"Ride Offer": ride}), 200


class GetAllRequestsToRideOffer(MethodView):
    @jwt_required
    def get(self, ride_id):
        if len(ride_id) > 0 and ride_id != None:
            validation = validate.validate_entered_id(ride_id)
            if validation:
                return jsonify({"message": validation}), 400
            ride_requests = get_requests_to_rideOffer(ride_id)
            return jsonify({"Ride Requests": ride_requests}), 200


class SendRideRequest(MethodView):
    @jwt_required
    def post(self, location, destination, ride_id):

        validation = validate.validate_LocationDestination(
            location, destination)
        validation2 = validate.validate_entered_id(ride_id)

        if validation:
            return jsonify({"message": validation}), 400

        if validation2:
            return jsonify({"message": validation2}), 400

        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M")

        loggedin_user = get_jwt_identity()
        user = get_user_by_username(username=loggedin_user)

        ride_id = ride_id
        client_id = user[0]
        client_name = user[1] + "" + user[2]
        client_contact = user[4]
        location = location
        destination = destination
        status = 'pending'

        send_ride_request(
            date=date,
            ride_id=ride_id,
            client_id=client_id,
            client_name=client_name,
            client_contact=client_contact,
            location=location,
            destination=destination,
            status=status)

        return jsonify({"Ride Requests": "Your Request has been sent"}), 200


class HandleRideRequest(MethodView):
    def put(self, status, request_id, ride_id):
        """function to reject or accept a ride request""" 
        validation = validate.validate_status(status)
        validation2 = validate.validate_entered_id(request_id)
        validation3 = validate.validate_entered_id(ride_id)

        if validation:
            return jsonify({"message": validation}), 400
        elif validation2:
            return jsonify({"message": validation2}), 400
        elif validation3:
            return jsonify({"message": validation3}), 400    


create_offer_view = CreateOffer.as_view('create_offer_view')

ride_blueprint.add_url_rule(
    '/api/v1/rides/create', view_func=create_offer_view, methods=['POST'])
