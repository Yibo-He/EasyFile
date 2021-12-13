import unittest
from app import create_app
import json
# from flask_testing import TestCase


class TestLogout(unittest.TestCase):
    """define a test class for Logout"""

    def setUp(self):
        self.app = create_app(r'D:\Downloads\EasyFile\instance\config.py')
        self.app.config['TESTING'] = True
        self.app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] = False
        self.client = self.app.test_client()
    
    def test_ok(self):
        """no errors found"""
        
        # 1 send empty data
        # create a post request to backend, data specifies the request.form, return a object
        response = self.client.post("/auth/logout", data={})
        resp_dict = json.loads(response.data)
        self.assertEquals(resp_dict, {'state': 0, 'info':'success'})





if __name__ == '__main__':
    unittest.main()