""" Object Classes modelling the system actors"""


class User:
	def __init__(self, firstName, secondName, userName, contact, user_category, password):
		self.firstName = firstName
		self.secondName = secondName
		self.userName = userName
		self.contact = contact
		self.user_category = user_category
		self.password = password


class Driver(User):
	def __init__(self,firstName, secondName, userName, contact, user_category, car_type, reg_num, lic_num,password):
		User.__init__(self,firstName, secondName, userName, contact, user_category, password)
		self.car_type = car_type
		self.reg_num = reg_num
		self.lic_num = lic_num


class RideOffer:
	def __init__(self, driver_name, location, car_type, plate_number, contact, availability, cost_per_km):
		"""Constructor to the RideOffer Class"""
		self.driver_name = driver_name
		self.location = location
		self.car_type = car_type
		self.plate_number = plate_number
		self.contact = contact
		self.availability = availability
		self.cost_per_km = cost_per_km

	def toJson(self):
		"""Function to give the RideOffer model ability to be jsonified """
		offer = dict(
			driver=self.driver_name,
			contact=self.contact,
			car_type=self.car_type,
			offerer_location=self.location,
			plate_number=self.plate_number,
			availability=self.availability,
			cost_per_km=self.cost_per_km
		)
		return offer


class RideRequest:
	def __init__(self, request_id, ride_id, client_id, passenger_name, contact, location, destination, status):
		""" Constructor to the RideRequest Class """
		self.request_id = request_id
		self.ride_id = ride_id
		self.client_id = client_id
		self.passenger_name = passenger_name
		self.contact = contact
		self.location = location
		self.destination = destination
		self.status = status



	def toJson(self):
		"""Function to give the RideRequest model ability to be jsonified """
		request = dict(
			id=self.id,
			passenger=self.passenger_name,
			contact=self.contact,
			location=self.location,

		)
		return request
