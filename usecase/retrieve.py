from typing import List
from core.domain.person.entitiy import Person
from repository.person_repository import PersonRepository


class RetrieveUseCase:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository

    def get_person(self, entityId: str) -> Person:
        person_data = self.person_repository.get_person(entityId)
        return Person(**person_data)

    def get_people(self) -> List[Person]:
        people_data = self.person_repository.get_people()
        return [Person(**person_data) for person_data in people_data]