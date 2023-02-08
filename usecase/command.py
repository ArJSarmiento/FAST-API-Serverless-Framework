from core.dto.person import PersonDTO
from core.domain.entities.person import Person
from core.exception.contact import ContactAlreadyExistsError

from external_gateway.hub_person_service import HubPersonService
from external_gateway.hub_address_service import HubAddressService
from external_gateway.hub_contact_details_service import HubContactService
from external_gateway.auth_service import Auth
from repository.person_repository import PersonRepository


# CommandUseCase is a use case that creates, updates, and deletes a person from the HubService and the PersonRepository
class CommandUseCase:
    def __init__(self, person_repository: PersonRepository, auth: Auth):
        self.person_repository = person_repository
        self.hub_person_service = HubPersonService(auth)
        self.hub_address_service = HubAddressService(auth)
        self.hub_contact_service = HubContactService(auth)

    async def create_person(self, request: PersonDTO) -> Person:
        person_data = request.dict()
        person = Person(**person_data)

        # create hub person object
        hub_person = person.generate_hub_person(generatePracticeId=True)
        hub_person_response = await self.hub_person_service.create_hub_person(hub_person)
        person.entryId = hub_person_response['entryId']

        # create hub contacts and addresses objects
        hub_mobile_contact = person.generate_mobile_contact()
        hub_home_email_contact = person.generate_home_contact()
        hub_office_email_contact = person.generate_office_contact()
        hub_home_address = person.generate_home_address()
        hub_office_address = person.generate_office_address()

        try:
            # push hub contacts and addresses to hub service
            await self.hub_contact_service.create_hub_contact(hub_mobile_contact)
            await self.hub_contact_service.create_hub_contact(hub_home_email_contact)
            await self.hub_contact_service.create_hub_contact(hub_office_email_contact)
            await self.hub_address_service.create_hub_address(hub_home_address)
            await self.hub_address_service.create_hub_address(hub_office_address)
        except Exception as e:
            # if any of the hub services fail, delete the person from the hub service
            await self.hub_person_service.delete_hub_person(person.entryId, hub_person_response['practiceId'])
            raise ContactAlreadyExistsError from e 

        # push person to person repository
        self.person_repository.create_person(person)
        return person

    async def update_person(self, entryId: str, practiceId: str, request: PersonDTO) -> Person:
        # create person object
        person_data = request.dict()
        person = Person(**person_data)
        person.entryId = entryId
        
        # create hub person object
        hub_person = person.generate_hub_person(generatePracticeId=False)
        hub_person.practiceId = practiceId

        await self.hub_person_service.update_hub_person(entryId, hub_person)

        # push person to person repository
        new_person_data = self.person_repository.update_person(entryId, person)
        return Person(**new_person_data)

    async def delete_person(self, entryId: str, practiceId: str) -> Person:
        # delete hub person, contacts, and addresses
        await self.hub_person_service.delete_hub_person(entryId, practiceId)
        
        person_data = self.person_repository.delete_person(entryId)
        return Person(**person_data)