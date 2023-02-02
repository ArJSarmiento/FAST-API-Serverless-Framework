from fastapi import Depends
from core.dto.person import PersonDTO
from core.domain.person import PersonDomain
from repository.person_repository import Person_Repository
from external_gateway import hub_service, auth_service
from uuid import uuid4

class CommandUseCase:
    def __init__(
        self,
        person_repository: Person_Repository = Depends(Person_Repository),
    ):
        self.person_repository = person_repository

    def create_person(self, request: PersonDTO):
        person_data = request.dict()
        person_data["personId"] = str(uuid4())
        person = PersonDomain.make(person_data)
        return self.person_repository.create_person(person)

    def update_person(self, personId: str, request: PersonDTO):
        person_data = request.dict()
        person_data.pop("personId", None)
        return self.person_repository.update_person(personId, person_data)

    def delete_person(self, personId: str) -> PersonDTO:
        return self.person_repository.delete_person(personId)