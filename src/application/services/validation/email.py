# class to validate email
import re
from domain.repositories.user_repository import UserRepository
from application.interfaces.validation.hunter_interface import HunterInterface

class EmailValidator:
    def __init__(self, email: str, user_repository: UserRepository = None):
        self.email = email
        self.user_repository = user_repository

    def is_valid(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def is_unique(self, email):
        if self.user_repository is None:
            raise Exception("User Repository not defined")
        else:
            return self.user_repository.find_by_email(email) is None

    def exists_in_web(self, email):
        hunter_interface = HunterInterface()
        return hunter_interface.verify_email(email)