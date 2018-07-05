# import unittest
# from run import app
# from flask import jsonify, json
# from app.models import Driver
# from app import views
# from app.db.dbManager import DBConnection

# my_connection = DBConnection()

# class Test_Ride_Offers(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()
#         my_connection.delete_tables()
#         my_connection.create_tables()


    
#     def test_adding_offer_with_empty_location(self):
#         """ Test for empty driver name validation """
        
#         response1 = self.app.post("/api/v1/user/register",
#                                  content_type='application/json',
#                                  data=json.dumps(dict(firstName="Natie", secondName="kyra", userName="araali",
#                                                       contact="0888887676", user_category="driver", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
#                                  )
#         response = self.app.post(
#             "/api/v1/user/login",
#             content_type='application/json',
#             data=json.dumps(dict(userName="araali", password="farooq"))
#         )
#         reply2 = json.loads(response.data.decode())

#         response2 = self.app.post("/api/v1/rides/create_offer",
#                                  content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
#                                  data=json.dumps(dict(location="",
#                                                       car_type="Benz", plate_number="uab 123x", contact="08887676", availability="10am - 10pm", cost_per_km="200"),)   
#                              ) 

#         reply = json.loads(response2.data)
#         self.assertEquals(reply["message"], "location is missing")
#         self.assertEquals(response.status_code, 400)  

#     # def test_adding_offer_with_empty_location(self):
#     #     """ Test for empty location validation """
#     #     response = self.app.post("/api/v1/rides/add_offer",
#     #         content_type='application/json',
#     #         data=json.dumps(dict(id="1",driver_name="Araali",location="",
#     #                             car_type="Benz",plate_number="uab 123x",contact="1672525252",availability="10am - 10pm",cost_per_km="200"),)
#     #         )  
#     #     reply = json.loads(response.data)
#     #     self.assertEquals(reply["message"], "Location is missing")
#     #     self.assertEquals(response.status_code, 400)

#     def test_adding_offer_with_empty_car_type(self):
#         """ Test for empty car type validation """
       
#         response = self.app.post(
#                 "/api/v1/rides/add_offer",
#             content_type='application/json',
#             data=json.dumps(dict(id="1",driver_name="Araali",location="kawempe",
#                                 car_type="",plate_number="uab 123x",contact="1672525252",availability="10am - 10pm",cost_per_km="200"),)
#             )  
#         reply = json.loads(response.data)
#         self.assertEquals(reply["message"], "Car type is missing")
#         self.assertEquals(response.status_code, 400)

#     def test_adding_offer_with_empty_plate_number(self):
#         """ Test for empty plate number validation """
        
#         response = self.app.post(
#                 "/api/v1/rides/add_offer",
#             content_type='application/json',
#             data=json.dumps(dict(id="1",driver_name="Araali",location="Wemps",
#                                 car_type="Benz",plate_number="",contact="1672525252",availability="10am - 10pm",cost_per_km="200"),)
#             )  
#         reply = json.loads(response.data)
#         self.assertEquals(reply["message"], "Plate number is missing")
#         self.assertEquals(response.status_code, 400)


#     def test_adding_offer_with_empty_contact(self):
#         """ Test for empty contact validation """
        
#         response = self.app.post(
#                 "/api/v1/rides/add_offer",
#             content_type='application/json',
#             data=json.dumps(dict(id="1",driver_name="Araali",location="Wemps",
#                                 car_type="Benz",plate_number="uab 234n",contact="",availability="10am - 10pm",cost_per_km="200"),)
#             )  
#         reply = json.loads(response.data)
#         self.assertEquals(reply["message"], "Contact is missing")
#         self.assertEquals(response.status_code, 400)  


#     def test_adding_offer_with_empty_availability(self):
#         """ Test for empty availability validation """
        
#         response = self.app.post(
#                 "/api/v1/rides/add_offer",
#             content_type='application/json',
#             data=json.dumps(dict(id="1",driver_name="Araali",location="Wemps",
#                                 car_type="Benz",plate_number="uab 234n",contact="6437484949",availability="",cost_per_km="200"),)
#             )  
#         reply = json.loads(response.data)
#         self.assertEquals(reply["message"], "Working hours not stated")
#         self.assertEquals(response.status_code, 400)  


#     def test_adding_offer_with_empty_cost_per_km(self):
#         """ Test for empty cost_per_km validation """
        
#         response = self.app.post(
#                 "/api/v1/rides/add_offer",
#             content_type='application/json',
#             data=json.dumps(dict(id="1",driver_name="Araali",location="Wemps",
#                                 car_type="Benz",plate_number="uab 234n",contact="6437484949",availability="10am - 10pm",cost_per_km=""),)
#             )  
#         reply = json.loads(response.data)
#         self.assertEquals(reply["message"], "Charge per Km not stated")
#         self.assertEquals(response.status_code, 400)  

    
    