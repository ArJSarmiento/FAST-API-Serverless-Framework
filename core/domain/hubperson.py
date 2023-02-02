from ..dto.response import HubPersonDTO
from usecase.hub_person_usecases import HubPersonUsecases

class HubPersonDomain:
    def __init__(self, hub_person_usecases: HubPersonUsecases):
        self.hub_person_usecases = hub_person_usecases

    def get_hub_person(self, hubPersonId: str) -> HubPersonDTO:
        return self.hub_person_usecases.get_hub_person(hubPersonId)

    def get_hub_people(self) -> list[HubPersonDTO]:
        return self.hub_person_usecases.get_hub_people()

    def create_hub_person(self, hub_person: HubPersonDTO) -> HubPersonDTO:
        return self.hub_person_usecases.create_hub_person(hub_person)

    def update_hub_person(self, hubPersonId: str, hub_person: HubPersonDTO) -> HubPersonDTO:
        return self.hub_person_usecases.update_hub_person(hubPersonId, hub_person)

    def delete_hub_person(self, hubPersonId: str) -> dict:
        return self.hub_person_usecases.delete_hub_person(hubPersonId)