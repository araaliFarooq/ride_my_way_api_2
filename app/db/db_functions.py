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
    query = (
        """INSERT INTO rideOffers (driver_id, date, driverName, location, carType, plateNumber, contact, availability, costPerKm) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".
        format(driver_id, date, driverName, location, carType, plateNumber,
                  contact, availability, costPerKm))
    cursor.execute(query)


# def get_a_single_user_request(self, request_id):
#         """ function to retrieve a single request from the database for a logged in user"""
#         self.cursor.execute("SELECT * FROM user_requests WHERE request_id = '{}'" .format(request_id))
#         req = self.cursor.fetchall()
#         if not req:
#             return {"msg": "request doesn't exist"}
#         return req

# def get_a_user_requests(self, username):
#         """ function to fetch all requests for a signed in user """
#         self.cursor.execute("SELECT * FROM user_requests WHERE request_owner = '{}'" .format(username))
#         req = self.cursor.fetchall()
#         if not req:
#             return {"msg": "No requests yet"}
#         return req

# def update_user_request(self, title, desc, request_id):
#         update_command = ("UPDATE user_requests SET request_title='{}', request_desc='{}' where request_id='{}'" .format(title, desc, int(request_id)))
#         self.cursor.execute(update_command)

# def get_all_app_requests(self):
#         self.cursor.execute("SELECT * from user_requests")
#         all_rows = self.cursor.fetchall()
#         return all_rows

# def update_request_status(self, request_id, request_status):
#         update_command = ("UPDATE user_requests SET request_status='{}' where request_id='{}'" .format(request_status, int(request_id)))
#         self.cursor.execute(update_command)
