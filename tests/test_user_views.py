import unittest
from app import views
from run import app
import json
from app.db.dbManager import DBConnection

my_connection = DBConnection()




class Test_Requests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        my_connection.delete_tables()
        my_connection.create_tables()

    
    def test_create_ride_offer(self):
        '''Test to create an offer'''
        response1 = self.app.post("/api/v1/user/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(firstName="Natie", secondName="kyra", userName="araali",
                                                      contact="0888887676", user_category="driver", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
                                 )
        response = self.app.post(
            "/api/v1/user/login",
            content_type='application/json',
            data=json.dumps(dict(userName="araali", password="farooq"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/rides/create_offer",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(location="kawempe",
                                                      car_type="Benz", plate_number="uab 123x", contact="08887676", availability="10am - 10pm", cost_per_km="200"),)   
                             )
        self.assertEquals(response2.status_code, 201)                     
 

    
    def test_request_to_join_offers(self):
        '''Test to request to join an offer'''
        
        response = self.app.post("/api/v1/user/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(firstName="Farooq", secondName="Minawa", userName="araali",
                                                      contact="0888887676", user_category="passenger", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
                                 )
        
        response = self.app.post("/api/v1/user/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(firstName="Natie", secondName="kyra", userName="araali",
                                                      contact="0888887676", user_category="driver", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
                                 )
        
        response1 = self.app.post(
            "/api/v1/user/login",
            content_type='application/json',
            data=json.dumps(dict(userName="araali", password="farooq"))
        )
        reply = json.loads(response1.data.decode())

        response3 = self.app.post("/api/v1/rides/create_offer",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply['token']),
                                 data=json.dumps(dict(location="kawempe",
                                                      car_type="Benz", plate_number="uab 123x", contact="08887676", availability="10am - 10pm", cost_per_km="200"),)   
                             )
        
        response2 = self.app.post("/api/v1/rides/send_request/kawempe/kampala/1",
                                 content_type='application/json',headers=dict(Authorization='Bearer '+reply['token']),
                                 )
        reply2 = json.loads(response2.data.decode())
        
        self.assertEquals(reply2["Ride Requests"], "Your Request has been sent")
        self.assertEquals(response2.status_code, 201)
    
    
    # def test_create_ride_offer(self):
        
    #     token = BaseTestCase().fetch_token()
    #     resp = BaseTestCase().add_ride()
    #     data = json.loads(resp.data.decode())
    #     self.assertEqual(resp.status_code,200)
