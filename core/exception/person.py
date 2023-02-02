from .exception import BaseError

class PersonNotFoundError(BaseError):
    def __init__(self, message: str):
        super().__init__(status_code=400, detail=message)
        self.message = 'Person not found.'

    
class PersonStatusError(BaseError):
    def __init__(self, message: str):
        super().__init__(status_code=500, detail=message)
        self.message = 'Person status error.'