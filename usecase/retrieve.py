from typing import List
from core.domain.hub_person.entity import HubPerson
from external_gateway.hub_service import Hub

# RetrieveUseCase is a use case that retrieves a person from the HubService
class RetrieveUseCase:
    def __init__(self, hub_service: Hub = None):
        self.hub_service = hub_service

    async def get_person(self, entryId: str, practice_id: str) -> HubPerson:
        hub_person_data = await self.hub_service.get_hub_person(entryId, practice_id)
        return HubPerson(**hub_person_data)

    async def get_people(self) -> List[HubPerson]:
        hub_people_data = await self.hub_service.get_all_hub_people()
        return [HubPerson(**person) for person in hub_people_data['items']]
