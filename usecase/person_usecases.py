from core.person import PersonModel
from repository import person_repository

def get_person(personId: str):
    return person_repository.get_person(personId)

def get_people():
    return person_repository.get_people()

def create_person(person: PersonModel):
    return person_repository.create_person(person)

def update_person(personId: str, person: PersonModel):
    return person_repository.update_person(personId, person)

def delete_person(personId: str) -> dict:
    return person_repository.delete_person(personId)