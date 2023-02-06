from data_store.person_dynamodb import PersonDynamoDB
from core.domain.person.entitiy import Person

class PersonRepository:
    def __init__(self, dynamodb: PersonDynamoDB):
        self.dynamodb = dynamodb

    def get_person(self, entityId: str) -> Person:
        return self.dynamodb.get_item(entityId)

    def get_person_by_attribute(self, attribute: str, value: str) -> Person:
        return self.dynamodb.get_item_by_attribute(attribute, value)

    def get_people(self) -> list[Person]:
        return self.dynamodb.get_items()

    def create_person(self, person: Person) -> Person:
        return self.dynamodb.create_item(person.to_dict())

    def update_person(self, entityId: str, person: Person) -> Person:
        return self.dynamodb.update_item(entityId, person.to_dict())

    def delete_person(self, entityId: str) -> Person:
        return self.dynamodb.delete_item(entityId)
