from pydantic import (
    BaseModel,
    constr
)


# Address DTO
class Address(BaseModel):
    line1: constr(max_length=256)
    line2: constr(max_length=256)
    city: constr(max_length=64)
    state: constr(max_length=64)
    postcode: constr(max_length=64)
    country: constr(max_length=64)
