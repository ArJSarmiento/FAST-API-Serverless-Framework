
from __future__ import annotations

from ..domain.person.entitiy import Person
from .person import PersonDTO
from .hubperson import HubPersonDTO


class PersonIn(PersonDTO):
    @classmethod
    def build_result(cls, person: Person):
        return cls(**person.to_dict())


class HubPersonIn(HubPersonDTO):
    @classmethod
    def build_result(cls, person: Person):
        return cls(**person.to_dict())
