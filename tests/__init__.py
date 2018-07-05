import unittest
from run import app
from app.db.dbManager import DBConnection
import json
import datetime

# my_connection = DBConnection


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        app.config["TESTING"] = True
        

    def login_user(self, username, password):
        with self.client:
            return self.client.post("/api/v1/user/login", data=json.dumps(dict(username="araali", 
                                password="farooq")), content_type="application/json")

    def fetch_token(self):
        resp = self.login_user("araali","farooq")
        data = json.loads(resp.data.decode())
        return data["token"]

    def add_ride(self):
        now = datetime.datetime.now()
        _date = now.strftime("%Y-%m-%d %H:%M")
        return self.app.post("/api/v1/rides/create_offer", data=json.dumps(dict(driver_id= 1, date = _date, driverName = 'driverName', location='location',carType = 'carType', 
        plateNumber = 'plateNumber',contact = 'contact', availability='availability', costPerKm='costPerKm')), content_type="application/json")
