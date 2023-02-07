# REST-API-Serverless-Framework

###  Technologies:
 - Python
 - DDD
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
pip install -r requirements.txt
```
2
```shell
serverless deploy
```
3.
```shell
uvicorn core.main:app --reload
```
   
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
