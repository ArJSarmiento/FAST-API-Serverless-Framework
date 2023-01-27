import os
import boto3
from boto3.dynamodb.conditions import Key, Attr
from fastapi import FastAPI, Body
from pydantic import BaseModel
from mangum import Mangum
from datetime import date
from fastapi.responses import HTMLResponse
from typing import Union
from uuid import uuid4

STAGE = os.environ.get('STAGE')
root_path = f'/{STAGE}' if STAGE else '/'
app = FastAPI(title="Integration API", root_path=root_path)

#  DynamoDB resource
dynamo_resource = boto3.resource("dynamodb")
person_table = dynamo_resource.Table("integration-person-arnel")

# Person model 
class PersonModel(BaseModel):
    person_id: Union[str, None] = None
    firstName: str
    lastName: str
    preferredName: str
    dateOfBirth: str
    gender: str
    maritalStatus: str
    mobileNumber: str
    homeEmail: str
    officeEmail: str
    homeAddress: str
    officeAddress: str
    
# root url
@app.get("/")
def welcome():
    html_content = """
    <html>
        <head>
            <title>Welcome to the Integration API</title>
        </head>
        <body>
            <h1>Welcome to the Integration API</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# retreive individual person
@app.get("/api/person/{person_id}")
def retreive_person(person_id: str):
    get_resp = person_table.get_item(Key={"person_id": person_id})
    if get_resp["ResponseMetadata"]["HTTPStatusCode"] != 200:
        return {"ok": False, "person": {}}
    return get_resp.get("Item")

# retreive all persons
@app.get("/api/person")
def retreive_people():
    response = person_table.scan()
    return response.get("Items")

# create person
@app.post("/api/person")
def create_person(person: PersonModel):
    person = person.dict()
    person["person_id"] = str(uuid4())
    response = person_table.put_item(Item=person)
    if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
        return {"ok": False, "person": {}}
    return person

# update person
@app.put("/api/person")
def update_person(person: PersonModel):
    person = person.dict()
    response = person_table.update_item(
        Key={
            "person_id": person["person_id"]
        }, 
        ReturnValues = "UPDATED_NEW"
    )

    if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
        return {"ok": False, "person": {}}
    return response

# Mangum Handler, this is so important
handler = Mangum(app)