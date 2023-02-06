from .exception import BaseError


class PersonNotFoundError(BaseError):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail = 'Person not found.'
        )

class PersonConflictError(BaseError):
    def __init__(self):
        super().__init__(
            status_code=409,
            detail='Person already exists.'
        )

class InvalidPersonError(BaseError):
    def __init__(self, message: str):
        super().__init__(status_code=400, detail=message)