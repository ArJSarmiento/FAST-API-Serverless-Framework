<div align="center" style="display:grid;place-items:center;">
<p>
    	<img width="80" src="https://api.mogenius.com/file/id/f7382e8b-be9a-4b6e-be70-cba7c3c664f2" alt="Fast Api Logo">
<img width="80" src="https://pngimg.com/uploads/plus/plus_PNG106.png">
	<img width="80" src="https://assets-global.website-files.com/60acbb950c4d66d0ab3e2007/60d841cfd24a7264a80c75fc_Serverless_logo.png" alt="Serverless Framework">
</p>
<h1>FastAPI with Serverless Framework</h1>
<p>A serverless REST API implemented with Clean Architecure and Domain Driven Design</p>
</div>

## Intro
I've adopted Clean Architecure and the DDD pattern for my recent FastAPI project. DDD makes it easier to implement complex domain problems. Improved readability and easy code correction have significantly improved productivity. As a result, stable project management has become possible. 

Using DDD makes it easy to maintain collaboration with domain experts, not only engineers.
- It is possible to prevent the mental model and the actual software from being dualized.
- Business logic is easy to manage.
- Infrastructure change is flexible.

## Architecture

I followed the [clean architecture style](http://blog.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/) and structure the codebase accordingly.

![cleanArchitecture image](https://cdn-images-1.medium.com/max/1600/1*B7LkQDyDqLN3rRSrNYkETA.jpeg)

_Image credit to [Thang Chung under MIT terms](https://github.com/thangchung/blog-core)_

Most important rule:
> Source code dependencies can only point inwards. Nothing in an inner circle can know anything at all about something in an outer circle. In particular, the name of something declared in an outer circle must not be mentioned by the code in the an inner circle. That includes, functions, classes. variables, or any other named software entity.

## Directory Structure:
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

###  Technologies:
 - Python
 - Domain Driven Design
 - Clean Architecture
 - AWS
 - Serverless Framework
   - https://www.serverless.com/framework/docs
 - RESTAPI via FASTAPI
   - https://fastapi.tiangolo.com/


## DynamoDB Design Access Patterns and Decision
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

## Setup Environment
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

## Run:
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
