import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend')))
from app import *
from flask import Flask

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app, context = create_app()
        self.client = self.app.test_client()

    def test_home_status_code(self):
        """Test que la route d'accueil renvoie un code de statut 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_prediction_post_request(self):
        """Test une requête POST valide sur /prediction"""
        data = {
            'area': 1200,
            'bedrooms': 3,
            'bathrooms': 2,
            'stories': 2,
            'mainroad': 'yes',
            'guestroom': 'no',
            'basement': 'yes',
            'watheat': 'no',
            'aircond': 'yes',
            'parkings': 1,
            'prefarea': 'yes',
            'furnishingstatus': 'furnished'
        }
        response = self.client.post('/prediction', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Predicted Price:', response.data)

    def test_invalid_data(self):
        """Test une requête POST avec des données invalides"""
        data = {
            'area': 'invalid',
            'bedrooms': 3,
            'bathrooms': 2,
            'stories': 2,
            'mainroad': 'yes',
            'guestroom': 'no',
            'basement': 'yes',
            'watheat': 'no',
            'aircond': 'yes',
            'parkings': 1,
            'prefarea': 'yes',
            'furnishingstatus': 'furnished'
        }
        response = self.client.post('/prediction', data=data)
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'Invalid input:', response.data)

if __name__ == '__main__':
    unittest.main()
