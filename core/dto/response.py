from __future__ import annotations

from ..domain.person.entitiy import Person
from ..domain.hub_person.entity import HubPerson
from .hubperson import HubPersonDTO
from .person import PersonDTO

# Output DTO for Person
class PersonOut(PersonDTO):
    @classmethod
    def build_result(cls, person: Person):
        return cls(**person.to_dict())

    # override class Config to add entryId
    class Config:
        schema_extra = {
            'example': {
                'entryId': 'string',
                **PersonDTO.Config.schema_extra['example']
            }
        }


# Output DTO for HubPerson
class HubPersonOut(HubPersonDTO):
    @classmethod
    def build_result(cls, person: HubPerson):
        return cls(**person.to_output_dict())
