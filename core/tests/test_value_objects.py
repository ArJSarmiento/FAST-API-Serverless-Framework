from core.domain.value_objects import DateOfBirth, MobileNumber, Email, Address, OwnerType, AddressType, ContactType
from core.exception.person import InvalidPersonError
import pytest

def test_throw_exception_with_invalid_day_date_of_birth():
    dateOfBirth = "2021-12-32"
    with pytest.raises(InvalidPersonError):
        DateOfBirth(dateOfBirth)
        
def test_throw_exception_with_invalid_month_date_of_birth():
    dateOfBirth = "2021-13-01"
    with pytest.raises(InvalidPersonError):
        DateOfBirth(dateOfBirth)

def test_throw_exception_with_invalid_year_date_of_birth():
    dateOfBirth = "20210-12-01"
    with pytest.raises(InvalidPersonError):
        DateOfBirth(dateOfBirth)

def test_throw_exception_with_invalid_date_of_birth_format():
    dateOfBirth= "2021/12/01"
    with pytest.raises(InvalidPersonError):
        DateOfBirth(dateOfBirth)

def test_throw_exception_with_invalid_mobile_number():
    mobileNumber= "+6912345678"
    with pytest.raises(InvalidPersonError):
        MobileNumber(mobileNumber)

def test_throw_exception_with_invalid_email_address():
    homeEmail= "exampleexample.com"
    with pytest.raises(InvalidPersonError):
        Email(homeEmail)

def test_create_address():
    line1 = "123 Test Street"
    line2 = "Test Suburb"
    city = "Test City"
    state = "Test State"
    postcode = "1234"
    country = "Test Country"
    address = Address(line1, line2, city, state, postcode, country)
    assert address.line1 == line1
    assert address.line2 == line2
    assert address.city == city
    assert address.state == state
    assert address.postcode == postcode
    assert address.country == country
    
def test_throw_exception_with_invalid_owner_type():
    ownerType = "Invalid"
    with pytest.raises(ValueError):
        OwnerType(ownerType)
        
def test_throw_exception_with_invalid_address_type():
    addressType = "Invalid"
    with pytest.raises(ValueError):
        AddressType(addressType)
        
def test_throw_exception_with_invalid_contact_type():
    contactType = "Invalid"
    with pytest.raises(ValueError):
        ContactType(contactType)
