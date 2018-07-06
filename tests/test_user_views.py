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
        '''Test to get request status'''
        
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
    
    
    def test_get_request_status(self):
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
        reply4 = json.loads(response2.data.decode())
        
        response4 = self.app.get("/api/v1/requests/status",
        content_type='application/json', headers=dict(Authorization='Bearer '+reply['token']),
            data=reply4)
        reply2 = json.loads(response4.data.decode())
        

        self.assertEquals(response4.status_code, 200)


    def test_accepting_request(self):
        '''Test to accepting a ride request'''
        
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
        reply4 = json.loads(response2.data.decode())
        
        response4 = self.app.put("/api/v1/rides/requests/status/accept/1/1",
        content_type='application/json', headers=dict(Authorization='Bearer '+reply['token']),
            data={"status":"accept", "request_id":"1", "ride_id":"1"})
        reply2 = json.loads(response4.data.decode())
        

        self.assertEquals(response4.status_code, 200)


    def test_rejecting_request(self):
        '''Test to reject a ride request'''
        
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
        reply4 = json.loads(response2.data.decode())
        
        response4 = self.app.put("/api/v1/rides/requests/status/reject/1/1",
        content_type='application/json', headers=dict(Authorization='Bearer '+reply['token']),
            data={"status":"accept", "request_id":"1", "ride_id":"1"})
        reply2 = json.loads(response4.data.decode())
        

        self.assertEquals(response4.status_code, 200) 


    def test_get_all_requests_to_ride_offer(self):
        '''Test to reject a ride request'''
        
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
        reply4 = json.loads(response2.data.decode())
        
        response4 = self.app.get("/api/v1/requests/all_requests/1",
        content_type='application/json', headers=dict(Authorization='Bearer '+reply['token']),
            data={"ride_id":"1"})
        reply2 = json.loads(response4.data.decode())
        

        self.assertEquals(response4.status_code, 200)


    def test_get_ride_offer_details(self):
        '''Test to get details of a single offer'''
        
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
        
        response4 = self.app.get("/api/v1/rides/view_single_offer/1",
        content_type='application/json', headers=dict(Authorization='Bearer '+reply['token']),
            data={"ride_id":"1"})

        self.assertEquals(response4.status_code, 200)



    def test_get_all_ride_offers(self):
        '''Test to get details of a single offer'''
        
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
        reply7 = json.loads(response3.data.decode())                     
        
        response4 = self.app.get("/api/v1/rides/view_all_offers",
        content_type='application/json', headers=dict(Authorization='Bearer '+reply['token']),
            )

        self.assertEquals(response4.status_code, 200)          

        
                