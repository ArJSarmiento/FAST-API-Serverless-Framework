from __future__ import annotations
from ..value_objects import Gender, MaritalStatus, DateOfBirth, MobileNumber, Email, Address, AddressType, OwnerType, ContactType
from .hub_address import HubAddress
from .hub_contact import HubContact
from .hub_person import HubPerson
from uuid import uuid4

# Entity for Person
class Person:
    def __init__(
            self, 
            firstName: str, 
            lastName: str, 
            dateOfBirth: str, 
            mobileNumber: str, 
            gender: str, 
            homeEmail: str, 
            homeAddress: dict, 
            preferredName: str = '', 
            maritalStatus: str = '', 
            officeEmail: str = '', 
            officeAddress: dict = None, 
            entryId: str = '', 
            **kwargs
        ):
        if officeAddress is None:
            officeAddress = {}
        self.entryId = entryId
        self.firstName = firstName
        self.lastName = lastName
        self.preferredName = preferredName
        self.dateOfBirth = DateOfBirth(dateOfBirth)
        self.gender = Gender(gender)
        self.maritalStatus = MaritalStatus(maritalStatus)
        self.mobileNumber = MobileNumber(mobileNumber)
        self.homeEmail = Email(homeEmail)
        self.officeEmail = Email(officeEmail)
        self.homeAddress = Address(**homeAddress)
        self.officeAddress = Address(**officeAddress)

    def __eq__(self, other: Person) -> bool:
        return self.entryId == other.entryId if isinstance(other, Person) else False

    def to_dict(self) -> dict:
        return {
            'entryId': self.entryId,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'preferredName': self.preferredName,
            'dateOfBirth': self.dateOfBirth.get_value_str(),
            'gender': self.gender.value,
            'maritalStatus': self.maritalStatus.value,
            'mobileNumber': self.mobileNumber.value,
            'homeEmail': self.homeEmail.value,
            'officeEmail': self.officeEmail.value,
            'homeAddress': self.homeAddress.to_dict(),
            'officeAddress': self.officeAddress.to_dict()
        }

    def to_input_dict(self) -> dict:
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'preferredName': self.preferredName,
            'dateOfBirth': self.dateOfBirth.get_value_str(),
            'gender': self.gender.value,
            'maritalStatus': self.maritalStatus.value,
            'mobileNumber': self.mobileNumber.value,
            'homeEmail': self.homeEmail.value,
            'officeEmail': self.officeEmail.value,
            'homeAddress': self.homeAddress.to_dict(),
            'officeAddress': self.officeAddress.to_dict()
        }
        
    def generate_home_address(self) -> HubAddress:
        return HubAddress(
            ownerId=self.entryId,
            addressType = AddressType.RESIDENTIAL.value,
            **self.homeAddress.to_dict()
        )
        
    def generate_office_address(self) -> HubAddress:
        return HubAddress(
            ownerId=self.entryId,
            addressType = AddressType.BUSINESS.value,
            **self.officeAddress.to_dict()
        )
        
    def generate_home_contact(self) -> HubContact:
        return HubContact(
            ownerId=self.entryId,
            ownerType=OwnerType.PEOPLE,
            contactType=ContactType.HOME_EMAIL.value,
            detail=self.homeEmail.value
        )
        
    def generate_office_contact(self) -> HubContact:
        return HubContact(
            ownerId=self.entryId,
            ownerType=OwnerType.PEOPLE,
            contactType=ContactType.WORK_EMAIL.value,
            detail=self.officeEmail.value
        )
    
    def generate_mobile_contact(self) -> HubContact:
        return HubContact(
            ownerId=self.entryId,
            ownerType=OwnerType.PEOPLE,
            contactType=ContactType.MOBILE_PHONE,
            detail=self.mobileNumber.value
        )
        
    def generate_hub_person(self, generatePracticeId:bool) -> HubPerson:
        return HubPerson(
            countryOfResidence =  self.homeAddress.country,
            practiceId = str(uuid4()) if generatePracticeId else '',
            **self.to_input_dict()
        )