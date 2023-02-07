from .exception import BaseError

# PersonNotFoundError is a custom error that is raised when a person is not found 
class PersonNotFoundError(BaseError):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail='Person not found.'
        )

# PersonInvalidError is a custom error that is raised when a person is invalid
class InvalidPersonError(BaseError):
    def __init__(self, message: str):
        super().__init__(status_code=400, detail=message)
