from pydantic import BaseModel
from typing import Union

class PersonModel(BaseModel):
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