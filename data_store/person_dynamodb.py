import boto3
from core.person import PersonModel
from uuid import uuid4

dynamo_resource = boto3.resource("dynamodb")
table = dynamo_resource.Table("integration-person-arnel")

def get_item(person_id: str) :
    response = table.get_item(Key={"person_id": person_id})
    return response["Item"]

def get_items() :
    response = table.scan()
    return response.get("Items")

def create_item(person: PersonModel) :
    data = person.dict()
    data["person_id"] = str(uuid4())
    table.put_item(Item=data)
    return data 

def update_item(person_id: str, person: PersonModel):
    person_data = person.dict()
    person_data.pop("person_id", None)
    response = table.update_item(
        Key={
              "person_id": person_id
        },
        UpdateExpression="SET " + ",".join([f"{k}=:{k}" for k in person_data.keys()]),
        ExpressionAttributeValues={f":{k}" : v for k, v in person_data.items()},
        ReturnValues="ALL_NEW"
    )
    return response["Attributes"]

def delete_item(person_id: str) :
    table.delete_item(Key={"person_id": person_id})
    return {"message": "Item deleted"}