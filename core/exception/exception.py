from fastapi import HTTPException
class BaseError(HTTPException):
    pass