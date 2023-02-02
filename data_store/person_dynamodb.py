import boto3
from core.dto.person import PersonDTO
from core.exception.person import PersonNotFoundError

class PersonDynamoDB:
    def __init__(self):
        self.dynamo_resource = boto3.resource("dynamodb")
        self.table = self.dynamo_resource.Table("integration-person-arnel")

    def get_item(self, personId: str) :
        response = self.table.get_item(Key={"personId": personId})
        if item_data := response.get("Item"):
            return item_data
        raise PersonNotFoundError 

    def get_items(self) :
        response = self.table.scan()
        return response.get("Items")

    def create_item(self, person_data: PersonDTO) :
        self.table.put_item(Item=person_data)
        return person_data 

    def update_item(self, personId: str, person_data: PersonDTO):
        response = self.table.update_item(
            Key={"personId": personId},
            UpdateExpression="SET " + ",".join([f"{k}=:{k}" for k in person_data]),
            ExpressionAttributeValues={f":{k}": v for k, v in person_data.items()},
            ReturnValues="ALL_NEW",
        )
        if item_data := response["Attributes"]:
            return item_data
        raise PersonNotFoundError

    def delete_item(self, personId: str):
        response = self.table.delete_item(Key={"personId": personId})
        if item_data := response.get("Attributes"):
            return item_data
        raise PersonNotFoundError