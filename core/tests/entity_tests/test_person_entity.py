from core.domain.person.entitiy import Person
from core.exception.person import InvalidPersonError
from uuid import uuid4

test_data = {
    'entryId': str(uuid4()),
    "firstName": "Arnel",
    "lastName": "Sarmiento",
    "preferredName": "Arnel Jan",
    "dateOfBirth": "2021-12-01",
    "gender": "Male",
    "maritalStatus": "Single",
    "mobileNumber": "+69123456789",
    "homeEmail": "example@example.com",
    "officeEmail": "example@example.com",
    "homeAddress": "Example",
    "officeAddress": "Example"
}


def test_create_person():
    person = Person(**test_data)
    assert person.to_dict() == test_data


def test_missing_data():
    missing_test_data = test_data.copy()
    missing_test_data.pop("firstName")
    try:
        Person(**missing_test_data)
    except TypeError:
        assert True
    else:
        assert False


def test_invalid_date_of_birth():
    invalid_test_data = test_data.copy()
    invalid_test_data["dateOfBirth"] = "2021-12-32"
    try:
        Person(**invalid_test_data)
    except InvalidPersonError:
        assert True
    else:
        assert False

    invalid_test_data["dateOfBirth"] = "2021-13-01"
    try:
        Person(**invalid_test_data)
    except InvalidPersonError:
        assert True
    else:
        assert False

    invalid_test_data["dateOfBirth"] = "20210-12-01"
    try:
        Person(**invalid_test_data)
    except InvalidPersonError:
        assert True
    else:
        assert False


def test_invalid_date_of_birth_format():
    invalid_test_data = test_data.copy()
    invalid_test_data["dateOfBirth"] = "2021/12/01"
    try:
        Person(**invalid_test_data)
    except InvalidPersonError:
        assert True
    else:
        assert False


def test_invalid_mobile_number():
    invalid_test_data = test_data.copy()
    invalid_test_data["mobileNumber"] = "+6912345678"
    try:
        Person(**invalid_test_data)
    except InvalidPersonError:
        assert True
    else:
        assert False


def test_invalid_email_address():
    invalid_test_data = test_data.copy()
    invalid_test_data["homeEmail"] = "exampleexample.com"
    try:
        Person(**invalid_test_data)
    except InvalidPersonError:
        assert True
    else:
        assert False
