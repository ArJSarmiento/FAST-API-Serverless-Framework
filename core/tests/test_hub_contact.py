import pytest
from core.domain.entities.hub_contact import HubContact

test_contact_data = {
    'ownerId': '1',
    'detail': '0412345678',
    'ownerType': 'People',
    'contactType': 'Mobile Phone',
}

def test_throw_exception_with_invalid_contact_type():
    test_contact_data_copy = test_contact_data.copy()
    test_contact_data_copy['contactType'] = 'Invalid'
    with pytest.raises(ValueError):
        HubContact(**test_contact_data_copy)
        
def test_throw_exception_with_invalid_owner_type():
    test_contact_data_copy = test_contact_data.copy()
    test_contact_data_copy['ownerType'] = 'Invalid'
    with pytest.raises(ValueError):
        HubContact(**test_contact_data_copy)
        
def test_throw_exception_with_invalid_data():
    test_contact_data_copy = test_contact_data.copy()
    test_contact_data_copy.pop('ownerId')
    with pytest.raises(TypeError):
        HubContact(**test_contact_data_copy)