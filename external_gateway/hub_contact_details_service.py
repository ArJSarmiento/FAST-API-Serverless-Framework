from core.domain.entities.hub_contact import HubContact
from core.exception.person import PersonNotFoundError
from .auth_service import Auth
from .hub_service import Hub
import aiohttp

class HubContactService(Hub):
    def __init__(self, auth: Auth):
        super().__init__(auth)
        self.contact_url = f"{self.base_url}/contact-details"
    
    async def get_hub_contact(self, hub_contact_id: str):
        # logic to get a contact from the hub service
        if self.access_token == '':
            await self.authenticate()

        params = {
            'entryId': hub_contact_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{self.contact_url}/{hub_contact_id}',
                    headers=self.headers,
                    params=params
            ) as response:
                return await self.response_handler(response, self.get_hub_contact, hub_contact_id)

    async def create_hub_contact(self, hub_contact: HubContact):
        # logic to create a contact in the hub service
        if self.access_token == '':
            await self.authenticate()

        contact = hub_contact.to_dict()

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    self.contact_url,
                    headers=self.headers,
                    json=contact
            ) as response:
                return await self.response_handler(response, self.create_hub_contact, hub_contact)

    async def update_hub_contact(self, hub_contact_id: str, hub_contact: HubContact):
        # logic to update a contact in the hub service
        if self.access_token == '':
            await self.authenticate()
            
        try:
            await self.get_hub_contact(hub_contact_id)
        except PersonNotFoundError:
            return None

        contact = hub_contact.to_dict()

        async with aiohttp.ClientSession() as session:
            async with session.patch(
                    f'{self.contact_url}/{hub_contact_id}',
                    headers=self.headers,
                    params={'entryId': hub_contact_id},
                    json=contact
            ) as response:
                return await self.response_handler(response, self.update_hub_contact, hub_contact_id, hub_contact)

    async def delete_hub_contact(self, hub_contact_id: str):
        # logic to delete a contact in the hub service
        if self.access_token == '':
            await self.authenticate()
            
        try:
            await self.get_hub_contact(hub_contact_id)
        except PersonNotFoundError:
            return None

        params = {
            'entryId': hub_contact_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                    f'{self.contact_url}/{hub_contact_id}',
                    headers=self.headers,
                    params=params
            ) as response:
                return await self.response_handler(response, self.delete_hub_contact, hub_contact_id)