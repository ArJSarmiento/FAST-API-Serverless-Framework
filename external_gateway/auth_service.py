from fastapi import HTTPException
import requests

class Auth:
    def __init__(self):
        self.token = None
        self.base_url='https://test-api.advicerevolution.com.au'
        self.auth_endpoint = f"{self.base_url}/users/login"
        self.fetch_token_endpoint = f"{self.base_url}/users/fetch-token"
        self.refresh_endpoint = f"{self.base_url}/users/refresh-token"
        self.appId = ''
        self.appSecret = ''
        self.authCode = ''
        self.access_token = ''
        self.refreshToken = ''
        self.headers = {
               "Authorization": f"Bearer {self.appSecret}"
        }

    async def login(self, username: str, password: str):
        params = {
            'appId': self.appId,
            'redirectCode': True
        }
        credentials = {
            "username": username,
            "password": password
        }
        response = await requests.post(self.auth_endpoint, 
                         params=params,
                         headers=self.headers,
                         json=credentials
                        )

        response.raise_for_status()

        data = response.json()

        if response.status_code == 200:
            self.authCode = data["authCode"]
            return self.authCode

    async def fetch_token(self, authCode: str):
        fetch_credentials = {
            "authCode": authCode,
            "appId": self.appId,
            "appSecret": self.appSecret
        }
        response = await requests.post(
            self.fetch_token_endpoint,
            headers=self.headers,
            json=fetch_credentials
        )
        response.raise_for_status()
        data = response.json()
        if response.status_code == 200:
            self.access_token = data["accessToken"]
            self.refresh_token = data["refreshToken"]
            return self.access_token
        
    async def refresh(self):
        credentials = {
            'username': self.username,
            'refreshToken': self.refresh_token,
            'appId': self.appId,
            'appSecret': self.appSecret
        }
        response = await requests.post(
            self.refresh_endpoint,
            headers=self.headers,
            json=credentials
        )
        response.raise_for_status()
        data = response.json()
        if response.status_code == 200:
            self.accessToken = data["accessToken"]
            return self.accessToken