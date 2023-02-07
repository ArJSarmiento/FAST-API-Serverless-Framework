from fastapi import HTTPException

# This is a base error class that all other errors will inherit from
class BaseError(HTTPException):
    pass
