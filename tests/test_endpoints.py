'''
test module
'''
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
    def test_getAllParcelOrders(self, client):
        response = client.get("/api/v1/parcels")
        assert response.status_code == 201
        
    def test_makeNewParcelOrder(self, client):    
        response = client.get("/api/v1/parcels")
        assert response.status_code == 201 
    def test_singleParcelOrder(id):
        response = client.get("/api/v1/parcels/<int:id>")
        assert response.status_code == 201   
    def test_updateParcelOrder(id):
        response = client.get("/api/v1/parcels/<int:id>")
        assert response.status_code == 201         