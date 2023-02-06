from core.config import settings
from core.domain.hub_person.entity import HubPerson
from .auth_service import Auth
from fastapi import HTTPException
from core.exception.person import PersonNotFoundError
from uuid import uuid4
import requests

class Hub:
    def __init__(self):
        self.auth = Auth()
        self.base_url = settings.APP_HUB_BASE_URL
        self.people_url = f"{self.base_url}/people"
        self.access_token = ''
        self.headers = {}

    async def authenticate(self):
        if self.auth.authCode == '':
            await self.auth.login()
            self.access_token = await self.auth.fetch_token()
        else:
            self.access_token = await self.auth.refresh_token()

        self.headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

    async def get_hub_person(self, hub_person_id: str, practice_id: str):
        # logic to call the get_hub_person endpoint of the hub service
        if self.access_token == '':
            await self.authenticate()

        params = {
            'entryId': hub_person_id,
            'practiceId': practice_id
        }
        response = requests.get(
            f'{self.people_url}/{hub_person_id}',
            headers=self.headers,
            params=params
        )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise PersonNotFoundError
        else:
            raise HTTPException(
                status_code=response.status_code, detail=response.json())

    async def get_all_hub_people(self):
        # logic to call the get_all_hub_persons endpoint of the hub service
        if self.access_token == '':
            await self.authenticate()

        response = requests.get(f'{self.people_url}/', headers=self.headers)

        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    async def create_hub_person(self, hub_person: HubPerson):
        # logic to call the create_hub_person endpoint of the hub service
        if self.access_token == '':
            await self.authenticate()

        person = hub_person.to_input_dict()
        person['practiceId'] = str(uuid4())

        response = requests.post(
            self.people_url,
            headers=self.headers,
            json=person
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code, detail=response.json())

    async def update_hub_person(self, hub_person_id: str, hub_person: HubPerson):
        # logic to call the update_Hub_person endpoint of the hub service
        if self.access_token == '':
            await self.authenticate()

        person = hub_person.to_input_dict()
        response = requests.patch(
            f'{self.people_url}/{hub_person_id}',
            headers=self.headers,
            params={'entryId': hub_person_id},
            json=person,
        )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise PersonNotFoundError
        else:
            raise HTTPException(
                status_code=response.status_code, detail=response.json())

    async def delete_hub_person(self, hub_person_id: str, practice_id: str):
        if self.access_token == '':
            await self.authenticate()

        params = {
            'entryId': hub_person_id,
            'practiceId': practice_id
        }
        response = requests.delete(
            f'{self.people_url}/{hub_person_id}',
            headers=self.headers,
            params=params
        )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise PersonNotFoundError
        else:
            raise HTTPException(
                status_code=response.status_code, detail=response.json())
