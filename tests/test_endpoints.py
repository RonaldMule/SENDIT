'''
test module
'''
from endpoints import app
from unittest import TestCase

class TestEndPoints(TestCase):
    """
    Test the endpoints
    """
    def setUp(self):
        self.app_tester = app.test_client()
        
    def test_makeNewParcelOrder(self):
        self.assertEqual(response.status_code,(201))