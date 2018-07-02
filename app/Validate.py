"""validating user input fields"""
from flask import jsonify


class FieldValidation:

	def client_validation(self, firstName, secondName, userName, contact, user_category, password):

		if len(firstName) < 1:
			return jsonify({"message": "First name is missing"}), 400
		if len(secondName) < 1:
			return jsonify({"message": "Second name is missing"}), 400
		if len(userName) < 1:
			return jsonify({"message": "Username is missing"}), 400
		if len(contact) < 1:
			return jsonify({"message": "Contact is missing"}), 400
		if len(user_category) < 1:
			return jsonify({"message": "User category is missing"}), 400
		if len(password) < 1:
			return jsonify({"message": "Password is missing"}), 400

	def driver_validation(self,  firstName, secondName, userName, contact, user_category, car_type, reg_num, lic_num, password):

		if len(firstName) < 1:
			return jsonify({"message": "First name is missing"}), 400
		if len(secondName) < 1:
			return jsonify({"message": "Second name is missing"}), 400
		if len(userName) < 1:
			return jsonify({"message": "Username is missing"}), 400
		if len(contact) < 1:
			return jsonify({"message": "Contact is missing"}), 400
		if len(user_category) < 1:
			return jsonify({"message": "User category is missing"}), 400
		if len(password) < 1:
			return jsonify({"message": "Password is missing"}), 400
		if len(car_type) < 1:
			return jsonify({"message": "Car type is missing"}), 400
		if len(reg_num) < 1:
			return jsonify({"message": "Registration number is missing"}), 400
		if len(lic_num) < 1:
			return jsonify({"message": "Licence number is missing"}), 400


	def login_validation(self, userName, password):
		if len(userName) < 1:
			return jsonify({"message": "Missing or Wrong username"}), 400
		if len(password) < 1:
			return jsonify({"message": "Missing or Wrong password"}), 400


	def offer_validation(self, driverName, location, carType, plateNumber, contact, availability, costPerKm):

		if len(driverName) < 1:
			return jsonify({"message": "Drivers name is missing"}), 400
		if len(location) < 1:
			return jsonify({"message": "Location is missing"}), 400
		if len(carType) < 1:
			return jsonify({"message": "Car type is missing"}), 400
		if len(plateNumber) < 1:
			return jsonify({"message": "Plate number is missing"}), 400
		if len(contact) < 1:
			return jsonify({"message": "Contact is missing"}), 400
		if len(availability) < 1:
			return jsonify({"message": "Working hours not stated"}), 400
		if len(costPerKm) < 1:
			return jsonify({"message": "Charge per Km not stated"}), 400