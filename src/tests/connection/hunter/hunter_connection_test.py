import unittest
from infrastructure.validation.hunter_connector import HunterConnector

class TestHunterConnection(unittest.TestCase):
    def test_connection(self):
        hunter_connector = HunterConnector()
        response = hunter_connector.connect()
        self.assertEqual(response["data"]["first_name"], "Marcio")
        
if __name__ == '__main__':
    unittest.main()