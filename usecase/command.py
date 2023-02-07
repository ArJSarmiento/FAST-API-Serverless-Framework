from core.dto.person import PersonDTO
from core.domain.person.entitiy import Person
from core.domain.hub_person.entity import HubPerson
from repository.person_repository import PersonRepository
from external_gateway.hub_service import Hub
from uuid import uuid4

# CommandUseCase is a use case that creates, updates, and deletes a person from the HubService and the PersonRepository
class CommandUseCase:
    def __init__(self, person_repository: PersonRepository, hub_service: Hub = None):
        self.person_repository = person_repository
        self.hub_service = hub_service

    async def create_person(self, request: PersonDTO) -> Person:
        person_data = request.dict()

        hub_person_data = person_data.copy()
        hub_person_data['countryOfResidence'] = person_data['homeAddress']['country']
        hub_person_data['practiceId'] = str(uuid4())
        hub_person = HubPerson(**hub_person_data)
        hub_person_response = await self.hub_service.create_hub_person(hub_person)

        person_data['entryId'] = hub_person_response['entryId']
        person = Person(**person_data)
        self.person_repository.create_person(person)

        return person

    async def update_person(self, entryId: str, request: PersonDTO) -> Person:
        person_data = request.dict()
        hub_person_data = person_data.copy()

        hub_person_data['countryOfResidence'] = person_data['homeAddress']['country']
        hub_person = HubPerson(**hub_person_data)
        await self.hub_service.update_hub_person(entryId, hub_person)

        person = Person(**person_data)
        new_person_data = self.person_repository.update_person(entryId, person)

        return Person(**new_person_data)

    async def delete_person(self, entryId: str, practiceId: str) -> Person:
        await self.hub_service.delete_hub_person(entryId, practiceId)
        person_data = self.person_repository.delete_person(entryId)
        return Person(**person_data)
