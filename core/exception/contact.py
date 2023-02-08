from .exception import BaseError
        
class ContactAlreadyExistsError(BaseError):
    def __init__(self):
        super().__init__(
            status_code=409,
            detail='Contact already exists.'
        )
    
class ContactNotFoundError(BaseError):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail='Contact not found.'
        )