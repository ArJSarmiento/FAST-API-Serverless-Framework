import re
from enum import Enum
from datetime import datetime
from ..exception.person import InvalidPersonError
from email_validator import validate_email, EmailNotValidError

# Value Objects


class Gender(Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"

    def __eq__(self, other):
        return self.value == other.value


class MaritalStatus(Enum):
    Single = "Single"
    Married = "Married"
    Divorced = "Divorced"
    Widowed = "Widowed"
    Separated = "Separated"
    Other = "Other"

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
    def __init__(self, value: str):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value
