from __future__ import annotations
import re
from enum import Enum
from datetime import datetime
from ..exception.person import InvalidPersonError
from email_validator import validate_email, EmailNotValidError

# Value Objects
class Gender(str, Enum):
    male="Male"
    female="Female"
    other="Other"

    def __eq__(self, other):
        return self.value == other.value


class MaritalStatus(str, Enum):
    single = "Single"
    married = "Married"
    deFacto = "De facto"

    def __eq__(self, other):
        return self.value == other.value


class DateOfBirth:
    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%Y-%m-%d")
        except ValueError as e:
            raise InvalidPersonError(
                "Invalid date format. Must be YYYY-MM-DD.") from e

    def __eq__(self, other):
        return self.value == other.value

    def get_value_str(self):
        return self.value.strftime("%Y-%m-%d")


class MobileNumber:
    def __init__(self, value: str):
        pattern = re.compile(r'^\+\d{1,3}\d{10}$')
        if not pattern.match(value):
            raise InvalidPersonError(
                "Invalid mobile number format. Must be in the format +XXXYYYYYYYYY, where XXX is the country code and YYYYYYYYYY is the mobile number.")
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class Email:
    def __init__(self, value: str):
        try:
            validation = validate_email(value, check_deliverability=False)
            email = validation.email
        except EmailNotValidError as e:
            raise InvalidPersonError("Invalid email format.") from e

        self.value = email

    def __eq__(self, other):
        return self.value == other.value


class Address:
    def __init__(
        self,
        line1: str,
        line2: str,
        city: str,
        state: str,
        postcode: str,
        country: str 
    ):
        try:
            self.line1 = line1
            self.line2 = line2
            self.city = city
            self.state = state
            self.postcode = postcode
            self.country = country
        except:
            raise InvalidPersonError("Invalid address format.")

    def __eq__(self, other: Address):
        return self.to_dict() == other.to_dict()
    
    def to_dict(self):
        return {
            'line1': self.line1,
            'line2': self.line2,
            'city': self.city,
            'state': self.state,
            'postcode': self.postcode,
            'country': self.country
        }
        
class OwnerType(str, Enum):
    PEOPLE = 'People'
    ENTITIES = 'Entities'

    def __eq__(self, other):
        return self.value == other.value
    
class AddressType(str, Enum):
    POSTAL = 'Postal'
    RESIDENTIAL = 'Residential'
    BUSINESS = 'Business'
    REGISTERED = 'Registered'
    
    def __eq__(self, other):
        return self.value == other.value

class ContactType(str, Enum):
    HOME_PHONE = 'Home Phone'
    WORK_PHONE = 'Work Phone'
    MOBILE_PHONE = 'Mobile Phone'
    OTHER_PHONE = 'Other Phone'
    HOME_EMAIL = 'Home Email'
    WORK_EMAIL = 'Work Email'
    OTHER_EMAIL = 'Other Email'
    
    def __eq__(self, other):
        return self.value == other.value