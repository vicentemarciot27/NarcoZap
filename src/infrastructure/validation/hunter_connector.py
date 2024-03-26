import requests
import os
from dotenv import load_dotenv

class HunterConnector:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("HUNTER_API_KEY")
        
    def connect(self):
        url = f"https://api.hunter.io/v2/account?api_key={self.api_key}"
        response = requests.get(url)
        return response.json()
        
    def verify_email(self, email):
        url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={self.api_key}"
        response = requests.get(url)
        return response.json()
    
# test the connector
hunter_connector = HunterConnector()
print(hunter_connector.connect())
print(hunter_connector.verify_email("marcim.pessoal@gmail.com"))
