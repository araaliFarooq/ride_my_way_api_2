"""Functions to interact with the db"""
from app.db.dbManager import DBConnection

connect = DBConnection()
cursor = connect.cursor


def add_new_client(firstName, secondName, userName, contact, password):
    query = (
        """INSERT INTO clients (firstName,secondName,userName,contact,password) VALUES ('{}', '{}', '{}', '{}', '{}')""".
        format(firstName, secondName, userName, contact, password))
    cursor.execute(query)


def add_new_driver(firstName, secondName, userName, contact, carType, reg_num,
                   lic_num, password):
    query = (
        """INSERT INTO drivers (firstName,secondName,userName,contact,carType, regNumber, licNumber,password) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".
        format(firstName, secondName, userName, contact, carType, reg_num,
               lic_num, password))
    cursor.execute(query)


def get_user_by_username(username):
    query = ("""SELECT * from clients where userName = '{}'""".format(username))
    cursor.execute(query)
    userName = cursor.fetchone()
    if userName == None:
        query = (
            """SELECT * from drivers where userName = '{}'""".format(username))
        cursor.execute(query)
        userName = cursor.fetchone()
        return userName
    else:
        return userName


def add_new_offer(driver_id, date, driverName, location, carType, plateNumber,
                  contact, availability, costPerKm):
    """function to add a new ride offer"""
    query = (
        """INSERT INTO rideOffers (driver_id, date, driverName, location, carType, plateNumber, contact, availability, costPerKm) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".
        format(driver_id, date, driverName, location, carType, plateNumber,
               contact, availability, costPerKm))
    cursor.execute(query)


def get_all_ride_offers():
    """function to get all registered offers"""
    cursor.execute("SELECT * from rideOffers")
    all_offers = cursor.fetchall()
    return all_offers


def get_rideoffer_details(ride_id):
    """ function to get details of a ride offer"""
    cursor.execute(
        "SELECT * FROM rideOffers WHERE ride_id = '{}'" .format(ride_id))
    rows = cursor.fetchone()
    if not rows:
        return {"message": "Offer doesn't exist"}
    return rows

def get_requests_to_rideOffer(ride_id):
    """ function to get requests to a ride offer """
    cursor.execute(
        "SELECT * FROM rideRequest WHERE ride_id = '{}'" .format(ride_id))
    requests = cursor.fetchall()
    if not requests:
        return {"message": "No requests exist"}
    return requests


def send_ride_request(date, ride_id, client_id, client_name, client_contact, location, destination, status):
    """function to submit a request made for a ride"""
    query = (
        """INSERT INTO rideRequests (date, ride_id, client_id, client_name, client_contact, location, destination, status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".
        format(date, ride_id, client_id, client_name, client_contact, location, destination, status))
    cursor.execute(query)


def handle_ride_request(status, request_id, ride_id):
    """function to accept or reject ride requests"""
    query = ("""UPDATE rideRequests SET status = '{}' where request_id = '{}' and ride_id = '{}'""" .format(
        status, request_id, ride_id))
    cursor.execute(query)

"""end of line"""