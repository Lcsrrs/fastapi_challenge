from pydantic import BaseModel
from typing import Optional

class Company:
    def __init__(self, name: str, address: str, phone: str, main_email: str):
        self.name = name
        self.address = address
        self.phone = phone
        self.main_email = main_email

class CompanyResponse(BaseModel):
    name: str
    address: str
    phone: str
    main_email: str

class CompanyEdit(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    main_email: Optional[str] = None

        