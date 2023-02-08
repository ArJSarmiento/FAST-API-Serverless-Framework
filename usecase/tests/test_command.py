import pytest
from uuid import uuid4
from unittest.mock import MagicMock, Mock
from core.dto.person import PersonDTO
from core.domain.entities.person import Person
from core.domain.entities.hub_person import HubPerson
from repository.person_repository import PersonRepository
from external_gateway.hub_person_service import HubPersonService
from usecase.command import CommandUseCase
import asyncio

test_data = {
    "entryId": str(uuid4()),
    "firstName": "string",
    "lastName": "string",
    "preferredName": "string",
    "dateOfBirth": "2023-02-07",
    "gender": "Male",
    "maritalStatus": "Single",
    "mobileNumber": "+639123456789",
    "homeEmail": "example@example.com",
    "officeEmail": "example@example.com",
    "homeAddress": {
        "line1": "string",
        "line2": "string",
        "city": "string",
        "state": "string",
        "postcode": "string",
        "country": "string"
    },
    "officeAddress": {
        "line1": "string",
        "line2": "string",
        "city": "string",
        "state": "string",
        "postcode": "string",
        "country": "string"
    }
}

pytest_plugins = ('pytest_asyncio')