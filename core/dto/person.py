from pydantic import BaseModel
from typing import Union
from datetime import datetime

class PersonDTO(BaseModel):
    personId: Union[str, None] = None
    firstName: str
    lastName: str
    preferredName: str
    dateOfBirth: str
    gender: str
    maritalStatus: str
    mobileNumber: str
    homeEmail: str
    officeEmail: str
    homeAddress: str
    officeAddress: str

    class Config:
        schema_extra = {
            'example': {
                'firstName': 'string',
                'lastName': 'string',
                'preferredName': 'string',
                'dateOfBirth': datetime.now().strftime("%Y/%m/%d"),
                'gender': 'Male',
                'maritalStatus': 'Single',
                'mobileNumber': '+639123456789',
                'homeEmail': 'string',
                'officeEmail': 'string',
                'homeAddress': 'string',
                'officeAddress': 'string'
            }
        }