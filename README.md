# REST-API-Serverless-Framework

###  Technologies:
 - Python
 - Domain Driven Design
 - Clean Architecture
 - AWS
 - Serverless Framework
   - https://www.serverless.com/framework/docs
 - RESTAPI via FASTAPI
   - https://fastapi.tiangolo.com/

# Setup Environment
## For Linux/Mac
### Installing venv 
```shell 
sudo apt-get install python3.9-venv
```
### Creating virtual env
```shell 
python -m venv env
```
### Activating virtual env
```shell 
source env/bin/activate
```
## For Windows
### Installing venv
```shell 
py -m pip install --user virtualenv
```
### Creating virtual env
```shell 
py -m venv env
```
### Activating virtual env
```shell 
.\env\Scripts\activate
```

# Run:
1.
```shell
npm install
```
2.
```shell
pip install -r requirements.txt
```
3.
```shell
serverless deploy
```
4.
```shell
uvicorn core.main:app --reload
```

### Test:
```shell
pytest -v
```

### DynamoDB Design Access Patterns and Decision
```shell
{
	'firstName': 'string',
	'lastName': 'string',
	'preferredName': 'string',
	'dateOfBirth': 2021-12-31,
	'gender': 'Male',
	'maritalStatus': 'Single',
	'mobileNumber': '+639123456789',
	'homeEmail': 'example@example.com',
	'officeEmail': 'example@example.com',
	'homeAddress': {
		'line1': 'string',
		'line2': 'string',
		'city': 'string',
		'state': 'string',
		'postcode': '8000',
		'country': 'Philippines',
	},
	'officeAddress': {
		'line1': 'string',
		'line2': 'string',
		'city': 'string',
		'state': 'string',
		'postcode': '8000',
		'country': 'Philippines',
	},
}
```
One DynamoDB table is sufficient to store information about the "Person Entity". The primary access pattern used to retrieve data from this table is by matching the "entryId" attribute with the corresponding "entryId" provided by the "Hub Service". This allows for quick and efficient retrieval and mutation of specific person records based on the unique identifier provided by the Hub Service.

   
### Directory Structure:
```tree
├── core
│   ├── (core logic)
├── usecase
│   ├── (directs communication between layers)
├── repository
│   ├── (translates between usecase and data_store)
├── controller
│   ├── (entry and exit points for the application)
├── external_gateway
│   ├── (all external communication)
├── data_store
│   ├── (Defines how data is stored)
```
