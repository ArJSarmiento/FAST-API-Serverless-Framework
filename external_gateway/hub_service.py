from core.config import settings
from .auth_service import Auth
from fastapi import HTTPException
from core.exception.contact import ContactNotFoundError

# Hub is a service that retrieves, creates, updates, and deletes a person from the HubService
class Hub:
    def __init__(self, auth: Auth):
        self.auth = auth
        self.base_url = settings.APP_HUB_BASE_URL
        self.access_token = auth.access_token
        self.headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

    async def authenticate(self):
        if self.auth.authCode == '':
            await self.auth.login()
        self.access_token = await self.auth.fetch_token()
        self.headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

    async def refresh_token(self):
        self.access_token = await self.auth.get_refresh_token()
        self.headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

    async def response_handler(self, response, func, *args, **kwargs):
        if response.status == 200:
            return await response.json()
        elif response.status == 404:
            raise ContactNotFoundError
        elif response.status == 401:
            await self.refresh_token()
            return await func(*args, **kwargs)
        else:
            raise HTTPException(
                status_code=response.status, detail=await response.json())