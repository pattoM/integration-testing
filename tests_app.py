import unittest
import requests
from requests import Session
from flask_sqlalchemy import SQLAlchemy
from app import db

class TestIntegration(unittest.TestCase):

    def test_valid_post(self):
        expression = "1 + 1"
        value = 2

        data = {"input":expression}

        req = requests.post('http://localhost:5000/add', data = data )
        

        response = req.input  #api response

        self.assertEqual(value, int(response[1]))


  

    def test_database_entry(self):
        entry_count = Expression.query().count()

        self.assertEqual(1, entry_count)

if __name__ == "__main__":
    unittest.main()
