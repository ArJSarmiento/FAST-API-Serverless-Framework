from pydantic import BaseModel

class PersonNotFoundError(BaseModel):
    message: str = "Person not found"
    
class ServerError(BaseModel):
    message: str