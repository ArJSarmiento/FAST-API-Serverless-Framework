from dataclasses import field
from typing import Any, TypeVar

EntityType = TypeVar("EntityType", bound="Entity")


class Entity:
    id: int = field(init=False)

    def __eq__(self, other: Any) -> bool:
        return self.id == other.id if isinstance(other, type(self)) else False

    def __hash__(self):
        return hash(self.id)


class AggregateRoot(Entity):
    """
    An entry point of aggregate.
    """
    pass
