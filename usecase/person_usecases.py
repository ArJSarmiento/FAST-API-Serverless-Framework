from core.person import PersonModel
from repository import person_repository

def get_person(person_id: str):
    return person_repository.get_person(person_id)

def get_people():
    return person_repository.get_people()

def create_person(person: PersonModel):
    return person_repository.create_person(person)

def update_person(person_id: str, person: PersonModel):
    return person_repository.update_person(person_id, person)

def delete_person(person_id: str) -> dict:
    return person_repository.delete_person(person_id)