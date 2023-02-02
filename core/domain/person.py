from __future__ import annotations

from dataclasses import dataclass, field
from .entity import AggregateRoot

@dataclass(eq=False)
class PersonDomain(AggregateRoot):
    personId: str = field(init=False)
    firstName: str = field(init=False)
    lastName: str = field(init=False)
    preferredName: str = field(init=False)
    dateOfBirth: str = field(init=False)
    gender: str = field(init=False)
    maritalStatus: str = field(init=False)
    mobileNumber: str = field(init=False)
    homeEmail: str = field(init=False)
    officeEmail: str = field(init=False)
    homeAddress: str = field(init=False)
    officeAddress: str = field(init=False)
    
    @classmethod
    def make(cls, person = dict) -> PersonDomain:
        return PersonDomain(**person)

    def update(self, person = dict) -> PersonDomain:
        for key, value in person.dict(exclude_unset=True).items():
            setattr(self, key, value)
        return self
    
    def delete(self) -> PersonDomain:
        return self