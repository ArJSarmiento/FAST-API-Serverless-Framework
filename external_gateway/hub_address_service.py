from core.domain.entities.hub_address import HubAddress
from core.exception.person import PersonNotFoundError
from .auth_service import Auth
from .hub_service import Hub
import aiohttp

class HubAddressService(Hub):
    def __init__(self, auth: Auth):
        super().__init__(auth)
        self.address_url = f"{self.base_url}/addresses"
    
    async def get_hub_address(self, hub_address_id: str):
        # logic to get a address from the hub service
        if self.access_token == '':
            await self.authenticate()

        params = {
            'entryId': hub_address_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{self.address_url}/{hub_address_id}',
                    headers=self.headers,
                    params=params
            ) as response:
                return await self.response_handler(response, self.get_hub_address, hub_address_id)

    async def create_hub_address(self, hub_address: HubAddress):
        # logic to create a address in the hub service
        if self.access_token == '':
            await self.authenticate()

        address = hub_address.to_dict()

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    self.address_url,
                    headers=self.headers,
                    json=address
            ) as response:
                return await self.response_handler(response, self.create_hub_address, hub_address)

    async def update_hub_address(self, hub_address_id: str, hub_address: HubAddress):
        # logic to update a address in the hub service
        if self.access_token == '':
            await self.authenticate()

        try:
            await self.get_hub_address(hub_address_id)
        except PersonNotFoundError:
            return None

        address = hub_address.to_dict()

        async with aiohttp.ClientSession() as session:
            async with session.patch(
                    f'{self.address_url}/{hub_address_id}',
                    headers=self.headers,
                    params={'entryId': hub_address_id},
                    json=address
            ) as response:
                return await self.response_handler(response, self.update_hub_address, hub_address_id, hub_address)

    async def delete_hub_address(self, hub_address_id: str):
        # logic to delete a address in the hub service
        if self.access_token == '':
            await self.authenticate()
            
        try:
            await self.get_hub_address(hub_address_id)
        except PersonNotFoundError:
            return None

        params = {
            'entryId': hub_address_id,
        }
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                    f'{self.address_url}/{hub_address_id}',
                    headers=self.headers,
                    params=params
            ) as response:
                return await self.response_handler(response, self.delete_hub_address, hub_address_id)