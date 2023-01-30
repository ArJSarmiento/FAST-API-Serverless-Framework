from data_store import person_dynamodb
from core.person import PersonModel

def get_person(personId: str) -> PersonModel:
    return person_dynamodb.get_item(personId)

def get_people() -> list[PersonModel]:
    return person_dynamodb.get_items()

def create_person(person: PersonModel) -> PersonModel:
    return person_dynamodb.create_item(person)

def update_person(personId: str, person: PersonModel) -> PersonModel:
    return person_dynamodb.update_item(personId, person)

def delete_person(personId: str) -> dict:
    return person_dynamodb.delete_item(personId)