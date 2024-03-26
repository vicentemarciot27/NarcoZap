# Entidade User com atributos como id, nome, contato, etc.
from datetime import datetime

class User:
    
    def __init__(self, id: int, name: str, contact: str, email: str, password: str, role: str, status: str, date_of_birth: datetime, created_at: datetime, updated_at: datetime):
        self.id = id
        self.name = name
        self.contact = contact
        self.email = email
        self.password = password
        self.role = role
        self.status = status
        self.date_of_birth = date_of_birth
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __str__(self):
        return f"User: {self.id} - {self.name} - {self.email} - {self.contact} / {self.role} - {self.status}"