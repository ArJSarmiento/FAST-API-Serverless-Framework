from core.domain.entities.hub_person import HubPerson
from core.exception.person import InvalidPersonError
from uuid import uuid4
import pytest

test_data = {
    'entryId': str(uuid4()),
    'entryStatus': "Active",
    "createDate": "2021-02-07",
    "updateDate": "2021-02-07",
    "createdBy": "string",
    "updatedBy": "string",
    'userGroup': 'Advice Practice', 
    'userRoles':["practice_manager", "adviser"],
    "firstName": "string",
    "lastName": "string",
    "practiceId": '12a2d2ff-987f-4dd2-a108-fa57987ed825',
    "dateOfBirth": "2023-02-07",
    "gender": "Male",
    "maritalStatus": "Single",
    "countryOfResidence": "Philippines",
}

test_input_data = {
    'userGroup': 'Advice Practice', 
    'userRoles':["practice_manager", "adviser"],
    "firstName": "string",
    "lastName": "string",
    "practiceId": '12a2d2ff-987f-4dd2-a108-fa57987ed825',
    "dateOfBirth": "2023-02-07",
    "gender": "Male",
    "maritalStatus": "Single",
    "countryOfResidence": "Philippines",
}


def test_create_hub_person_output_data():
    hub_person = HubPerson(**test_data)
    assert hub_person.to_output_dict() == test_data
    
def test_create_hub_person_input_data():
    hub_person = HubPerson(**test_data)
    assert hub_person.to_input_dict() == test_input_data
    
def test_create_hub_person_throw_exception_with_missing_data():
    test_data.pop('firstName')
    with pytest.raises(TypeError):
        HubPerson(**test_data)