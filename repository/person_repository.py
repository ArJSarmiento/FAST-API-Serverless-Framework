from data_store.person_dynamodb import PersonDynamoDB
from core.dto.person import PersonDTO
from fastapi import Depends

class Person_Repository:
    def __init__(self, person_dynamodb:PersonDynamoDB = Depends(PersonDynamoDB)):
        self.person_dynamodb = person_dynamodb
        
    def get_person(self, personId: str) -> PersonDTO:
        return self.person_dynamodb.get_item(personId)

    def get_people(self) -> list[PersonDTO]:
        return self.person_dynamodb.get_items()

    def create_person(self, person: PersonDTO) -> PersonDTO:
        return self.person_dynamodb.create_item(person)

    def update_person(self, personId: str, person: PersonDTO) -> PersonDTO:
        return self.person_dynamodb.update_item(personId, person)

    def delete_person(self, personId: str) -> PersonDTO:
        return self.person_dynamodb.delete_item(personId)