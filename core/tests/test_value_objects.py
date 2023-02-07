from core.domain.value_objects import DateOfBirth, MobileNumber, Email, Address
from core.exception.person import InvalidPersonError

def test_invalid_date_of_birth():
    dateOfBirth = "2021-12-32"
    try:
        DateOfBirth(dateOfBirth)
    except InvalidPersonError:
        assert True
    else:
        assert False

    dateOfBirth = "2021-13-01"
    try:
        DateOfBirth(dateOfBirth)
    except InvalidPersonError:
        assert True
    else:
        assert False

    dateOfBirth = "20210-12-01"
    try:
        DateOfBirth(dateOfBirth)
    except InvalidPersonError:
        assert True
    else:
        assert False


def test_invalid_date_of_birth_format():
    dateOfBirth= "2021/12/01"
    try:
        DateOfBirth(dateOfBirth)
    except InvalidPersonError:
        assert True
    else:
        assert False


def test_invalid_mobile_number():
    mobileNumber= "+6912345678"
    try:
        MobileNumber(mobileNumber)
    except InvalidPersonError:
        assert True
    else:
        assert False


def test_invalid_email_address():
    homeEmail= "exampleexample.com"
    try:
        Email(homeEmail)
    except InvalidPersonError:
        assert True
    else:
        assert False