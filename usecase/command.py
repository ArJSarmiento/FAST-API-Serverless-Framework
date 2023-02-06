from core.dto.person import PersonDTO
from core.domain.person.entitiy import Person
from repository.person_repository import PersonRepository
from uuid import uuid4
from core.exception.person import PersonConflictError

class CommandUseCase:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository

    def create_person(self, request: PersonDTO) -> Person:
        person_data = request.dict()
        person_data['entityId'] = str(uuid4())
        person = Person(**person_data)
        self.person_repository.create_person(person)
            
        return person

    def update_person(self, entityId: str, request: PersonDTO) -> Person:
        person_data = request.dict()
        person = Person(**person_data)
        self.person_repository.update_person(entityId, person)
        return person

    def delete_person(self, entityId: str) -> Person:
        person_data = self.person_repository.delete_person(entityId)
        return Person(**person_data)