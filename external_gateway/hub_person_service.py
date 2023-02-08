from core.domain.entities.hub_person import HubPerson
from .auth_service import Auth
from .hub_service import Hub
import aiohttp

# Hub is a service that retrieves, creates, updates, and deletes a person from the HubService
class HubPersonService(Hub):
    def __init__(self, auth: Auth):
        super().__init__(auth)
        self.people_url = f"{self.base_url}/people"

    async def get_hub_person(self, hub_person_id: str, practice_id: str):
        # logic to retrieve a person from the hub service
        if self.access_token == '':
            await self.authenticate()

        params = {
            'entryId': hub_person_id,
            'practiceId': practice_id
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{self.people_url}/{hub_person_id}',
                    headers=self.headers,
                    params=params
            ) as response:
                return await self.response_handler(response, self.get_hub_person, hub_person_id, practice_id)

    async def get_all_hub_people(self):
        # logic to retrieve all people from the hub service
        if self.access_token == '':
            await self.authenticate()

        params = {
            'entryStatus': 'ACTIVE',
            'pageSize': 100
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{self.people_url}/',
                    headers=self.headers,
                    params=params
            ) as response:
                return await self.response_handler(response, self.get_all_hub_people)

    async def create_hub_person(self, hub_person: HubPerson):
        # logic to create a person in the hub service
        if self.access_token == '':
            await self.authenticate()

        person = hub_person.to_input_dict()

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    self.people_url,
                    headers=self.headers,
                    json=person
            ) as response:
                return await self.response_handler(response, self.create_hub_person, hub_person)

    async def update_hub_person(self, hub_person_id: str, hub_person: HubPerson):
        # logic to update a person in the hub service
        if self.access_token == '':
            await self.authenticate()

        person = hub_person.to_input_dict()

        async with aiohttp.ClientSession() as session:
            async with session.patch(
                    f'{self.people_url}/{hub_person_id}',
                    headers=self.headers,
                    params={'entryId': hub_person_id},
                    json=person
            ) as response:
                return await self.response_handler(response, self.update_hub_person, hub_person_id, hub_person)

    async def delete_hub_person(self, hub_person_id: str, practice_id: str):
        # logic to delete a person in the hub service
        if self.access_token == '':
            await self.authenticate()

        params = {
            'entryId': hub_person_id,
            'practiceId': practice_id
        }
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                    f'{self.people_url}/{hub_person_id}',
                    headers=self.headers,
                    params=params
            ) as response:
                return await self.response_handler(response, self.delete_hub_person, hub_person_id, practice_id)