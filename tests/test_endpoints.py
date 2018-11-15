'''
test module
'''
from flask import  json
from endpoints import app
import pytest

@pytest.fixture()
def client():
    test_client = app.test_client()
    return test_client
class TestEndPoints:
    """
    Test the endpoints
    """
    def test_makeNewParcelOrder(self, client):    
        response = client.post("/api/v1/parcels", data=json.dumps({
        "parcel_weight":"100kg",
        "pickup_location":"Gulu",
        "destination": "humbug",
        "price" : 20000,
       "status":"malaba"}))
        assert response.status_code == 201 
    def test_getAllParcelOrders(self, client):
        response = client.post("/api/v1/parcels", data=json.dumps({
        "parcel_weight":"100kg",
        "pickup_location":"Gulu",
        "destination": "humbug",
        "price" : 20000,
       "status":"malaba"}))
        assert response.status_code == 201 
        response = client.get("/api/v1/parcels")
        assert response.status_code == 201
        
    
    #def test_singleParcelOrder():
     #   response = client.post("/api/v1/parcels", data=json.dumps({
     # "parcel_weight":"100kg",
      ## "destination": "humbug",
        #"price" : 20000,
       ##assert response.status_code == 201 
        #response = client.get("/api/v1/parcels/1")
        #assert response.status_code == 201   
    #def test_updateParcelOrder():
     #   response = client.put("/api/v1/parcels/{}".format(1))
      #  assert response.status_code == 201    
          