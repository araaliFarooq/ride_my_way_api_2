"""validating user input fields"""
from flask import jsonify
import re


class FieldValidation:

    def client_validation(self, firstName, secondName, userName, contact, user_category, password):

        if not firstName:
            return jsonify({"message": "first name is missing"}), 400
        if not secondName:
            return jsonify({"message": "second name is missing"}), 400
        if not userName:
            return jsonify({"message": "username is missing"}), 400
        if not contact:
            return jsonify({"message": "contact is missing"}), 400
        if not user_category:
            return jsonify({"message": "user category is missing"}), 400
        if not password:
            return jsonify({"message": "password is missing"}), 400

        if not contact.isdigit():
            return jsonify({"message": "contact should only be in digits"}), 400

    def driver_validation(self,  firstName, secondName, userName, contact, user_category, car_type, reg_num, lic_num, password):

        if not firstName:
            return jsonify({"message": "first name is missing"}), 400
        if not secondName:
            return jsonify({"message": "second name is missing"}), 400
        if not userName:
            return jsonify({"message": "username is missing"}), 400
        if not contact:
            return jsonify({"message": "contact is missing"}), 400
        if not user_category:
            return jsonify({"message": "user category is missing"}), 400
        if not password:
            return jsonify({"message": "password is missing"}), 400
        if not car_type:
            return jsonify({"message": "car type is missing"}), 400
        if not reg_num:
            return jsonify({"message": "registration number is missing"}), 400
        if not lic_num:
            return jsonify({"message": "licence number is missing"}), 400

    def login_validation(self, userName, password):
        if not userName:
            return jsonify({"message": "missing or wrong username"}), 400
        if not password:
            return jsonify({"message": "missing or wrong password"}), 400

    def offer_validation(self, driverName, location, carType, plateNumber, contact, availability, costPerKm):

        if not driverName :
            return jsonify({"message": "drivers name is missing"}), 400
        if not location:
            return jsonify({"message": "location is missing"}), 400
        if not carType:
            return jsonify({"message": "car type is missing"}), 400
        if not plateNumber:
            return jsonify({"message": "plate number is missing"}), 400
        if not contact:
            return jsonify({"message": "contact is missing"}), 400
        if not availability:
            return jsonify({"message": "working hours not stated"}), 400
        if not costPerKm:
            return jsonify({"message": "charge per Km not stated"}), 400

    def validate_entered_id(self, id):
        try:
            ride_id = int(id)
        except ValueError:
            return jsonify({"message": "id should be an interger"}), 400

    def validate_LocationDestination(self, location, destination):
        if not location or not destination:
            return jsonify({"message": "please provide both your location and destination"}), 400
        if not destination.isalnum() or not location.isalnum():
            return jsonify({"message": "location or destination should not have numbers"}), 400

    def validate_status(self, status):
        if not status:
            return jsonify({"message": "no status is provided"}), 400
        if not status.isalnum():
            return jsonify({"message": "status should not have numbers"}), 400
