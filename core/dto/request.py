
from __future__ import annotations

from ..domain.entities.person import Person
from .person import PersonDTO

# Input DTO for Person
class PersonIn(PersonDTO):
    @classmethod
    def build_result(cls, person: Person):
        return cls(**person.to_dict())