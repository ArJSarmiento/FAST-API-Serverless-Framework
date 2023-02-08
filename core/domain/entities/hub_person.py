from __future__ import annotations

# Entity for HubPerson
class HubPerson:
    def __init__(
        self, 
        firstName: str, 
        lastName: str,
        dateOfBirth: str = '',
        maritalStatus: str = '',
        gender: str = '',
        countryOfResidence: str = '',
        entryId: str = '', 
        entryStatus: str = '', 
        createDate: str = '', 
        updateDate: str = '', 
        createdBy: str = '', 
        updatedBy: str = '', 
        userGroup: str = 'Advice Practice', 
        userRoles: list[str] = None, 
        practiceId: str = '', 
        **kwargs
    ):
        if userRoles is None:
            userRoles = ["practice_manager", "adviser"]
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
        self.dateOfBirth = dateOfBirth
        self.maritalStatus = maritalStatus
        self.gender = gender
        self.countryOfResidence = countryOfResidence

    def __eq__(self, other: HubPerson) -> bool:
        return self.entryId == other.entryId if isinstance(other, HubPerson) else False

    def to_output_dict(self) -> dict:
        return {
            'entryId': self.entryId,
            'entryStatus': self.entryStatus,
            'createDate': self.createDate,
            'updateDate': self.updateDate,
            'createdBy': self.createdBy,
            'updatedBy': self.updatedBy,
            'userGroup': self.userGroup,
            'userRoles': self.userRoles,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'practiceId': self.practiceId,
            'dateOfBirth': self.dateOfBirth,
            'maritalStatus': self.maritalStatus,
            'gender': self.gender,
            'countryOfResidence': self.countryOfResidence
        }

    def to_input_dict(self) -> dict:
        input_dict = {
                'userGroup': self.userGroup,
                'userRoles': self.userRoles,
                'firstName': self.firstName,
                'lastName': self.lastName,
                'dateOfBirth': self.dateOfBirth,
                'maritalStatus': self.maritalStatus,
                'gender': self.gender,
                'countryOfResidence': self.countryOfResidence
            }
        if self.practiceId != '':
            input_dict['practiceId'] = self.practiceId
        return input_dict
