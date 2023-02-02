from __future__ import annotations

from ..domain.person import PersonDomain
from .person import PersonDTO

class PersonResponse(PersonDTO):
    @classmethod
    def build_result(cls, reservation: PersonDomain) -> PersonDTO:
        return PersonDTO(**reservation.__dict__)