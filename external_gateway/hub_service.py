from core.dto.person import PersonDTO
from .auth_service import Auth
from fastapi import HTTPException
import requests


class Hub:
    def __init__(self, auth=Auth()):
        self.auth = auth
        self.base_url = 'https://test-api.advicerevolution.com.au/hub/api/v1'
        self.people_url = f"{self.base_url}/people"
        self.headers = {
            "Authorization": f"Bearer {self.auth.access_token}"
        }

    async def get_PersonDTO(self, PersonDTO_id: str):
        # logic to call the get_PersonDTO endpoint of the hub service
        params = {
            'entryId': PersonDTO_id,
            'praticeId': 1
        }
        response = requests.get(
            self.people_url,
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    async def get_all_PersonDTOs(self):
        # logic to call the get_all_PersonDTOs endpoint of the hub service
        response = requests.get(f'{self.people_url}/', headers=self.headers)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    async def create_PersonDTO(self, PersonDTO: PersonDTO):
        # logic to call the create_PersonDTO endpoint of the hub service
        person = PersonDTO.dict()
        response = requests.post(
            self.people_url,
            headers=self.headers,
            json=person
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    async def update_PersonDTO(self, PersonDTO_id: str, PersonDTO: PersonDTO):
        # logic to call the update_PersonDTO endpoint of the hub service
        person = PersonDTO.dict()
        response = requests.patch(
            f'{self.people_url}/{PersonDTO_id}',
            headers=self.headers,
            params={'entryId': PersonDTO_id},
            json=person,
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    async def delete_PersonDTO(self, PersonDTO_id: str):
        params = {
            'entryId': PersonDTO_id,
            'practiceId': 1
        }
        response = requests.delete(
            f'{self.people_url}/{PersonDTO_id}',
            headears=self.headers,
            params=params
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
