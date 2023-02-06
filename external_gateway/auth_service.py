from fastapi import HTTPException
import requests


class Auth:
    def __init__(self):
        self.token = None
        self.base_url = 'https://test-api.advicerevolution.com.au'
        self.auth_endpoint = f"{self.base_url}/users/login"
        self.fetch_token_endpoint = f"{self.base_url}/users/fetch-token"
        self.refresh_endpoint = f"{self.base_url}/users/refresh-token"
        self.appId = '08fefa1d-ded2-4770-9331-0af969c8ea06'
        self.appSecret = '0Xv7OXsdOYeyb39GzDJUWsUKHQySRwQbvTo8UUWKrk5BXrl_KjSgeTosD41dDtL-I6pDsLhlYFsMivyVQDrjCjMBAwBzyGvdgsb_-i2Oa7TSjhL-jdc5Er368C1GamCR'
        self.username = "407fb21d-d862-4cfb-a390-7786060781d3"
        self.password = "T*zd24SHo!GdMeBh"
        self.authCode = ''
        self.access_token = ''
        self.refreshToken = ''
        self.headers = {
            "Authorization": f"Bearer {self.appSecret}"
        }

    async def login(self):
        params = {
            'appId': self.appId,
            'redirectCode': True
        }
        credentials = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(
            self.auth_endpoint,
            params=params,
            headers=self.headers,
            json=credentials
        )

        response.raise_for_status()

        data = response.json()

        if response.status_code == 200:
            self.authCode = data["authCode"]
            return self.authCode

    async def fetch_token(self):
        fetch_credentials = {
            "authCode": self.authCode,
            "appId": self.appId,
            "appSecret": self.appSecret
        }
        response = requests.post(
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

    async def refresh_token(self):
        credentials = {
            'username': self.username,
            'refreshToken': self.refresh_token,
            'appId': self.appId,
            'appSecret': self.appSecret
        }
        response = requests.post(
            self.refresh_endpoint,
            headers=self.headers,
            json=credentials
        )
        response.raise_for_status()
        data = response.json()
        if response.status_code == 200:
            self.accessToken = data["accessToken"]
            return self.accessToken
