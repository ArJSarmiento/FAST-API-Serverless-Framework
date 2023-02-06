from core.dto.person import PersonDTO
from core.domain.person.entitiy import Person
from core.domain.hub_person.entity import HubPerson
from repository.person_repository import PersonRepository
from uuid import uuid4
from external_gateway.hub_service import Hub

class CommandUseCase:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository

    def create_person(self, request: PersonDTO) -> Person:
        person_data = request.dict()
        person_data['entryId'] = str(uuid4())
        person = Person(**person_data)
        self.person_repository.create_person(person)
        return person

    def update_person(self, entryId: str, request: PersonDTO) -> Person:
        person_data = request.dict()
        person = Person(**person_data)
        self.person_repository.update_person(entryId, person)
        return person

    def delete_person(self, entryId: str) -> Person:
        person_data = self.person_repository.delete_person(entryId)
        return Person(**person_data)