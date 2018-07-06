from flask import jsonify, request, Blueprint
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.validate import FieldValidation
from app.models import RideOffer, RideRequest
from app.db.db_functions import add_new_offer, get_user_by_username, get_all_ride_offers, get_rideoffer_details, get_requests_to_rideOffer, send_ride_request, handle_ride_request, get_requests_status
import datetime

validate = FieldValidation()
ride_blueprint = Blueprint("ride_blueprint", __name__)


class CreateOffer(MethodView):
    """ class for creating a new ride offer """

    @jwt_required
    def post(self):
        # get entered data
        offer_data = request.get_json()
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M")

        loggedin_user = get_jwt_identity()
        user = get_user_by_username(username=loggedin_user)

        driver_id = user[0]
        driver_name = user[1] + " " + user[2]
        location = offer_data.get("location")
        car_type = offer_data.get("car_type")
        plate_number = offer_data.get("plate_number")
        contact = offer_data.get("contact")
        availability = offer_data.get("availability")
        cost_per_km = offer_data.get("cost_per_km")
        # validation
        response = validate.offer_validation(driver_name, location, car_type,
                                             plate_number, contact,
                                             availability, cost_per_km)
        if response:
            return response

        # storing entered request
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
        return jsonify({'New Offer Added': new_offer.__dict__}), 201


class ViewAllOffers(MethodView):
    @jwt_required
    def get(self):
        """function to get all offers"""
        all_offers = get_all_ride_offers()
        return jsonify({"All Offers": all_offers}), 200


class GetRideOfferDetails(MethodView):
    @jwt_required
    def get(self, ride_id):
        if len(ride_id) > 0 and ride_id != None:

            validation = validate.validate_entered_id(ride_id)
            if validation:
                return validation
            ride = get_rideoffer_details(ride_id=ride_id)
            return jsonify({"Ride Offer": ride}), 200


class GetAllRequestsToRideOffer(MethodView):
    @jwt_required
    def get(self, ride_id):
        if len(ride_id) > 0 and ride_id != None:
            validation = validate.validate_entered_id(ride_id)
            if validation:
                return validation
            ride_requests = get_requests_to_rideOffer(ride_id)
            return jsonify({"Ride Requests": ride_requests}), 200


class SendRideRequest(MethodView):
    @jwt_required
    def post(self, location, destination, ride_id):

        validation = validate.validate_LocationDestination(
            location, destination)
        validation2 = validate.validate_entered_id(ride_id)

        if validation:
            return validation

        if validation2:
            return validation2

        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M")

        loggedin_user = get_jwt_identity()
        user = get_user_by_username(username=loggedin_user)

        ride_id = ride_id
        client_id = user[0]
        client_name = user[1] + " " + user[2]
        client_contact = user[4]
        location = location
        destination = destination
        status1 = 'pending'

        send_ride_request(
            date=date,
            ride_id=ride_id,
            client_id=client_id,
            client_name=client_name,
            client_contact=client_contact,
            location=location,
            destination=destination,
            status=status1)

        return jsonify({"Ride Requests": "Your Request has been sent"}), 201


class HandleRideRequest(MethodView):
    @jwt_required
    def put(self, status, request_id, ride_id):
        """function to reject or accept a ride request"""
        validation = validate.validate_status(status)
        validation2 = validate.validate_entered_id(request_id)
        validation3 = validate.validate_entered_id(ride_id)

        if validation:
            return validation
        elif validation2:
            return validation2
        elif validation3:
            return validation3

        status = status
        ride_id = ride_id
        request_id = request_id

        if status == "accept":
            handle_ride_request(status='Accepted',
                                request_id=request_id, ride_id=ride_id)

        elif status == "reject":
            handle_ride_request(status='Rejected',
                                request_id=request_id, ride_id=ride_id)

        return jsonify({"Request": status}), 200

class GetRequestStatus(MethodView):
    """function to get a request status"""
    @jwt_required
    def get(self):
        loggedin_user = get_jwt_identity()
        user = get_user_by_username(loggedin_user)
        client_id = user[0]
        status = get_requests_status(client_id = client_id)
        return jsonify({"Request Status": status}), 200


get_request_status_view = GetRequestStatus.as_view('get_request_status_view')
create_offer_view = CreateOffer.as_view('create_offer_view')
view_offers_view = ViewAllOffers.as_view('view_offers_view')
get_offerdetails_view = GetRideOfferDetails.as_view('get_offerdetails_view')
get_requests_to_offer_view = GetAllRequestsToRideOffer.as_view(
    'get_requests_to_offer_view')
send_ride_request_view = SendRideRequest.as_view('send_ride_request_view')
handle_ride_request_view = HandleRideRequest.as_view(
    'handle_ride_request_view')

# endpoint to create ride offes
ride_blueprint.add_url_rule(
    '/api/v1/requests/status', view_func=get_request_status_view, methods=['GET'])

ride_blueprint.add_url_rule(
    '/api/v1/rides/create_offer', view_func=create_offer_view, methods=['POST'])

ride_blueprint.add_url_rule(
    '/api/v1/rides/view_all_offers', view_func=view_offers_view, methods=['GET'])

ride_blueprint.add_url_rule(
    '/api/v1/rides/view_single_offer/<ride_id>', view_func=get_offerdetails_view, methods=['GET'])

ride_blueprint.add_url_rule(
    '/api/v1/requests/all_requests/<ride_id>', view_func=get_requests_to_offer_view, methods=['GET'])

ride_blueprint.add_url_rule(
    '/api/v1/rides/send_request/<location>/<destination>/<ride_id>', view_func=send_ride_request_view, methods=['POST'])

ride_blueprint.add_url_rule(
    '/api/v1/rides/requests/status/<status>/<request_id>/<ride_id>', view_func=handle_ride_request_view, methods=['PUT'])
