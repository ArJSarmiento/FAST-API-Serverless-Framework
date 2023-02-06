from pydantic import (
    BaseModel, 
    StrictStr
)
from typing import Union
from datetime import datetime


class PersonDTO(BaseModel):
    entryId: Union[str, None] = None
    firstName: StrictStr
    lastName: StrictStr
    preferredName: StrictStr
    dateOfBirth: str
    gender: StrictStr
    maritalStatus: StrictStr
    mobileNumber: str
    homeEmail: StrictStr
    officeEmail: StrictStr
    homeAddress: StrictStr
    officeAddress: StrictStr

    class Config:
        schema_extra = {
            'example': {
                'firstName': 'string',
                'lastName': 'string',
                'preferredName': 'string',
                'dateOfBirth': datetime.now().strftime("%Y-%m-%d"),
                'gender': 'Male',
                'maritalStatus': 'Single',
                'mobileNumber': '+639123456789',
                'homeEmail': 'string',
                'officeEmail': 'string',
                'homeAddress': 'string',
                'officeAddress': 'string'
            }
        }
