from __future__ import annotations
from ..value_objects import Gender, MaritalStatus, DateOfBirth, MobileNumber, Email, Address
from enum import Enum


class HubPerson:
    def __init__(
        self,
        entryId: str = '',
        entryStatus: str = '',
        createDate: str = '',
        updateDate: str = '',
        createdBy: str = '',
        updatedBy: str = '',
        firstName: str = '',
        lastName: str = '',
        userGroup: str = 'Advice Practice',
        userRoles: list[str] = ["practice_manager", "adviser"],
        practiceId: str = '',
        **kwargs
    ):
        self.entryId = entryId
        self.entryStatus = entryStatus
        self.createDate = createDate
        self.updateDate = updateDate
        self.createdBy = createdBy
        self.updatedBy = updatedBy
        self.userGroup = userGroup
        self.userRoles = userRoles
        self.firstName = firstName
        self.lastName = lastName
        self.practiceId = practiceId

    def __eq__(self, other: HubPerson) -> bool:
        return self.entryId == other.entryId if isinstance(other, HubPerson) else False

    def to_output_dict(self) -> dict:
        return self.__dict__

    def to_input_dict(self) -> dict:
        data = self.__dict__
        data.pop('createDate')
        data.pop('updateDate')
        data.pop('createdBy')
        data.pop('updatedBy')
        data.pop('entryStatus')
        data.pop('entryId')
        return data
