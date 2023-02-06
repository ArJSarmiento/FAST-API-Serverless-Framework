from typing import List
from core.domain.person.entitiy import Person
from core.domain.hub_person.entity import HubPerson
from repository.person_repository import PersonRepository
from external_gateway.hub_service import Hub
from external_gateway.auth_service import Auth

class RetrieveUseCase:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository

    async def get_person(self, entryId: str) -> HubPerson:        
        person_data = self.person_repository.get_person(entryId)
        return Person(**person_data)

    async def get_people(self) -> List[Person]:
        auth_service= Auth()
        await auth_service.login()
        await auth_service.fetch_token()
        hub_service = Hub(auth_service)
        
        hub_people_data = await hub_service.get_all_PersonDTOs()
        self.person_repository.get_people()
        
        return [HubPerson(**person) for person in hub_people_data['items']]