from pydantic import (
    BaseModel,
    constr,
)
from typing import Optional
from datetime import datetime

# HubPerson DTO
class HubPersonDTO(BaseModel):
    entryId: constr(strict=True) 
    entryStatus: constr(strict=True) 
    createDate: constr(strict=True) 
    updateDate: constr(strict=True) 
    createdBy: constr(strict=True) 
    updatedBy: constr(strict=True) 
    userGroup: constr(strict=True) 
    userRoles: list[constr(strict=True)]
    firstName: constr(strict=True)
    lastName: constr(strict=True) 
    practiceId: constr(strict=True) 
    dateOfBirth: Optional[constr(strict=True)]
    maritalStatus: Optional[constr(strict=True)]
    gender: Optional[constr(strict=True)]
    countryOfResidence: Optional[constr(strict=True, max_length=64)]

    class Config:
        schema_extra = {
            'example': {
                'entryId': 'string',
                'entryStatus': 'string',
                'createDate': datetime.now().strftime("%Y-%m-%d"),
                'updateDate': datetime.now().strftime("%Y-%m-%d"),
                'createdBy': 'string',
                'updatedBy': 'string',
                'userGroup': 'string',
                'userRoles': ['string'],
                'firstName': 'string',
                'lastName': 'string',
                'practiceId': 'string',
                'dateOfBirth': datetime.now().strftime("%Y-%m-%d"),
                'maritalStatus': 'string',
                'gender': 'string',
                'countryOfResidence': 'string',
            }
        }
    