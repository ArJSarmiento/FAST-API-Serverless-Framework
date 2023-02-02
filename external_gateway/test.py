import requests

# Endpoint for authentication API
base_url = 'https://test-api.advicerevolution.com.au'
auth_endpoint = f"{base_url}/users/login"
appId = '08fefa1d-ded2-4770-9331-0af969c8ea06'
appSecret = '0Xv7OXsdOYeyb39GzDJUWsUKHQySRwQbvTo8UUWKrk5BXrl_KjSgeTosD41dDtL-I6pDsLhlYFsMivyVQDrjCjMBAwBzyGvdgsb_-i2Oa7TSjhL-jdc5Er368C1GamCR'

# Credentials for authentication API
credentials = {
  "username": "407fb21d-d862-4cfb-a390-7786060781d3",
  "password": "T*zd24SHo!GdMeBh"
}

headers = {
    "Authorization": f"Bearer {appSecret}"
}

params = {
    'appId': appId,
    'redirectCode': True
    }

# Request the access token
response = requests.post(auth_endpoint, 
                         params=params,
                         headers=headers,
                         json=credentials
                        )

# Extract the access token from the response
authCode = response.json()["authCode"]
print("Auth Code:", authCode)

fetch_token_endpoint = f"{base_url}/users/fetch-token"
fetch_credentials = {
    "authCode": authCode,
    "appId": appId,
    "appSecret": appSecret
}
    
response = requests.post(
    fetch_token_endpoint,
    headers=headers,
    json=fetch_credentials
)

access_token = response.json()["accessToken"]
refresh_token = response.json()["refreshToken"]

# # Endpoint for HUB API
hub_endpoint = f"{base_url}/hub/api/v1/people"


# Request data from the HUB API with the access token
headers = {
    "Authorization": f"Bearer {access_token}"
}

hub_response = requests.get(hub_endpoint, headers=headers)

# Handle the response from the HUB API
if hub_response.status_code == 200:
    data = hub_response.json()
    print("Data received:", data)
else:
    print("Error:", hub_response.text)