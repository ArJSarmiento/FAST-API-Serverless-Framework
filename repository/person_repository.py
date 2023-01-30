from data_store import person_dynamodb
from core.person import PersonModel

def get_person(person_id: str) -> PersonModel:
    return person_dynamodb.get_item(person_id)

def get_people() -> list[PersonModel]:
    return person_dynamodb.get_items()

def create_person(person: PersonModel) -> PersonModel:
    return person_dynamodb.create_item(person)

def update_person(person_id: str, person: PersonModel) -> PersonModel:
    return person_dynamodb.update_item(person_id, person)

def delete_person(person_id: str) -> dict:
    return person_dynamodb.delete_item(person_id)