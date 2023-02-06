import unittest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from core.dto.response import PersonOut
from core.dto.request import PersonIn

from usecase.command import CommandUseCase
from usecase.retrieve import RetrieveUseCase

from repository.person_repository import PersonRepository
from data_store.person_dynamodb import PersonDynamoDB


class TestPersonController(unittest.TestCase):

    def setUp(self):
        self.mock_dynamodb = PersonDynamoDB('test-table')
        self.repository = PersonRepository(self.mock_dynamodb)
        self.retrieve_usecase = RetrieveUseCase(self.repository)
        self.command_usecase = CommandUseCase(self.repository)
        self.app = TestPersonController.create_app(
            self.retrieve_usecase, self.command_usecase)
        self.client = TestClient(self.app)

    def test_retrieve_person(self):
        entryId = '123'
        self.mock_dynamodb.get_person.return_value = {
            'id': entryId, 'name': 'John Doe'}
        response = self.client.get(f'/api/person/{entryId}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), PersonOut(
            id=entryId, name='John Doe').dict())
