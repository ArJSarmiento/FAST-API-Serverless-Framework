import pytest
from core.domain.entities.hub_address import HubAddress

test_address_data = {
    'ownerId': '1',
    'line1': '123 Main Street',
    'line2': 'Unit 1',
    'city': 'Sydney',
    'state': 'NSW',
    'postcode': '2000',
    'country': 'Australia',
    'addressType': 'Residential',
    'ownerType': 'People',
}

def test_throw_exception_with_invalid_address_type():
    test_address_data_copy = test_address_data.copy()
    test_address_data_copy['addressType'] = 'Invalid'
    with pytest.raises(ValueError):
        HubAddress(**test_address_data_copy)
    
def test_throw_exception_with_invalid_owner_type():
    test_address_data_copy = test_address_data.copy()
    test_address_data_copy['ownerType'] = 'Invalid'
    with pytest.raises(ValueError):
        HubAddress(**test_address_data_copy)
        
def test_throw_exception_with_invalid_data():
    test_address_data_copy = test_address_data.copy()
    test_address_data_copy.pop('ownerId')
    with pytest.raises(TypeError):
        HubAddress(**test_address_data_copy)