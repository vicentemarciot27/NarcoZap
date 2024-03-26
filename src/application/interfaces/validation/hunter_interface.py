# class to validate hunter data
# from src.application.interfaces.validation.hunter_interface import HunterInterface
# PATH: src/application/services/validation/hunter.py

from application.interfaces.http_interface import HttpInterface
from infrastructure.validation.hunter_connector import HunterConnector

class HunterValidator:
    def __init__(self, email: str, http_interface: HttpInterface = None):
        self.email = email
        self.http_interface = http_interface
        self.hunter_connector = HunterConnector()
        self.connection = self.hunter_connector.connect()
        
    def verify_email(self, email):
        return self.hunter_connector.verify_email(email)