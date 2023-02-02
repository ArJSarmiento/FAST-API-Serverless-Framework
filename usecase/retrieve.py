from typing import List
from fastapi import Depends
from core.domain.person import PersonDomain 
from repository.person_repository import Person_Repository

class RetrieveUseCase:
    def __init__(
        self,
        person_repository: Person_Repository = Depends(Person_Repository),
    ):
        self.person_repository = person_repository

    def get_person(self, personId: str) :
        return self.person_repository.get_person(personId)

    def get_people(self) :
        return self.person_repository.get_people()