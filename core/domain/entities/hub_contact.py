from __future__ import annotations
from core.domain.value_objects import OwnerType, ContactType

class HubContact:
    def __init__(
        self,
        ownerId: str,
        detail: str,
        contactType: str,
        ownerType: str = OwnerType.PEOPLE.value,
    ):
        self.ownerId = ownerId
        self.ownerType = OwnerType(ownerType)
        self.contactType = ContactType(contactType)
        self.detail = detail
    
    def to_dict(self):
        return {
            'ownerId': self.ownerId,
            'ownerType': self.ownerType.value,
            'contactType': self.contactType.value,
            'detail': self.detail,
        }