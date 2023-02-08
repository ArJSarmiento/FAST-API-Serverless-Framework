from __future__ import annotations
from ..value_objects import AddressType, OwnerType

# Entity for HubAddress
class HubAddress:
    def __init__(
        self,
        ownerId: str,
        line1: str,
        line2: str,
        city: str,
        state: str,
        postcode: str,
        country: str,
        addressType: str,
        ownerType: str = OwnerType.PEOPLE.value,
        isCurrent: bool = True,
    ):
        self.ownerId = ownerId
        self.ownerType = OwnerType(ownerType)
        self.addressType = AddressType(addressType)
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country
        self.isCurrent = isCurrent
    
    def to_dict(self):
        return {
            'ownerId': self.ownerId,
            'ownerType': self.ownerType.value,
            'addressType': self.addressType.value,
            'line1': self.line1,
            'line2': self.line2,
            'city': self.city,
            'state': self.state,
            'postcode': self.postcode,
            'country': self.country,
            'isCurrent': self.isCurrent,
        }