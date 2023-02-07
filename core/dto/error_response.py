from pydantic import BaseModel

# Custom error response DTO
class PersonNotFoundError(BaseModel):
    message: str = "Person not found"

class ServerError(BaseModel):
    message: str
