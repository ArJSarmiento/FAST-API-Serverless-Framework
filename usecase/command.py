from core.dto.person import PersonDTO
from core.domain.person.entitiy import Person
from core.domain.hub_person.entity import HubPerson
from repository.person_repository import PersonRepository
from uuid import uuid4
from external_gateway.hub_service import Hub


class CommandUseCase:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository
        self.hub_service = Hub()

    async def create_person(self, request: PersonDTO) -> Person:
        person_data = request.dict()
        hub_person = HubPerson(**person_data)
        hub_person = await self.hub_service.create_hub_person(hub_person)

        person_data['entryId'] = hub_person['entryId']
        person = Person(**person_data)

        self.person_repository.create_person(person)
        return person

    async def update_person(self, entryId: str, request: PersonDTO) -> Person:
        person_data = request.dict()
        person = Person(**person_data)
        hub_person = HubPerson(**person_data)
        
        await self.hub_service.update_hub_person(entryId, hub_person)
        
        new_person_data = self.person_repository.update_person(entryId, person)
        return Person(**new_person_data)

    async def delete_person(self, entryId: str, practiceId: str) -> Person:
        await self.hub_service.delete_hub_person(entryId, practiceId)
        person_data = self.person_repository.delete_person(entryId)
        return Person(**person_data)
