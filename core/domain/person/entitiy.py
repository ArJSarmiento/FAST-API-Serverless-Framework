from __future__ import annotations
from ..value_objects import Gender, MaritalStatus, DateOfBirth, MobileNumber, Email, Address
from enum import Enum
 
class Person:
    def __init__(
        self,
        entityId: str,
        firstName: str,
        lastName: str,
        preferredName: str,
        dateOfBirth: str,
        gender: str,
        maritalStatus: str,
        mobileNumber: str,
        homeEmail: str,
        officeEmail: str,
        homeAddress: str,
        officeAddress: str
    ):
        self.entityId = entityId
        self.firstName = firstName
        self.lastName = lastName
        self.preferredName = preferredName
        self.dateOfBirth = DateOfBirth(dateOfBirth)
        self.gender = Gender(gender)
        self.maritalStatus = MaritalStatus(maritalStatus)
        self.mobileNumber = MobileNumber(mobileNumber)
        self.homeEmail = Email(homeEmail)
        self.officeEmail = Email(officeEmail)
        self.homeAddress = Address(homeAddress)
        self.officeAddress = Address(officeAddress)
    
    def __eq__(self, other:Person) -> bool:
        return self.entityId == other.entityId if isinstance(other, Person) else False

    def to_dict(self) -> dict:
        return {
            'entityId': self.entityId,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'preferredName': self.preferredName,
            'dateOfBirth': self.dateOfBirth.get_value_str(),
            'gender': self.gender.value,
            'maritalStatus': self.maritalStatus.value,
            'mobileNumber': self.mobileNumber.value,
            'homeEmail': self.homeEmail.value,
            'officeEmail': self.officeEmail.value,
            'homeAddress': self.homeAddress.value,
            'officeAddress': self.officeAddress.value
        }