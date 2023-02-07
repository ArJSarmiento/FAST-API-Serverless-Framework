from pydantic import (
    BaseModel,
    constr,
)
from typing import Optional
from datetime import datetime

from core.domain.value_objects import Gender, MaritalStatus
from .address import Address
    
# Person DTO
class PersonDTO(BaseModel):
    entryId: Optional[constr(strict=True)]
    firstName: constr(strict=True, max_length=64)
    lastName: constr(strict=True, max_length=64)
    preferredName: Optional[constr(strict=True, max_length=64)]
    dateOfBirth: str
    gender: Gender
    maritalStatus: Optional[MaritalStatus]
    mobileNumber: constr(strict=True, max_length=64)
    homeEmail: constr(strict=True, max_length=64)
    officeEmail: Optional[constr(strict=True, max_length=64)]
    homeAddress: Address
    officeAddress: Optional[Address]

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
                'homeEmail': 'example@example.com',
                'officeEmail': 'example@example.com',
                'homeAddress': {
                    'line1': 'string',
                    'line2': 'string',
                    'city': 'string',
                    'state': 'string',
                    'postcode': 'string',
                    'country': 'string',
                },
                'officeAddress': {
                    'line1': 'string',
                    'line2': 'string',
                    'city': 'string',
                    'state': 'string',
                    'postcode': 'string',
                    'country': 'string',
                },
            }
        }
