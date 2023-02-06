from pydantic import BaseModel


class HubPersonDTO(BaseModel):
    entryId: str
    entryStatus: str
    createDate: str
    updateDate: str
    createdBy: str
    updatedBy: str
    firstName: str
    lastName: str
    userGroup: str
    userRoles: list[str]
    practiceId: str
    adviserId: str
    clientGroupId: str
    title: str
    middleName: str
    preferredName: str
    dateOfBirth: str
    maritalStatus: str
    gender: str
    housingStatus: str
    residencyStatus: str
    isTaxResident: bool
    countryOfResidence: str
    countryOfCitizenship: str
    countryOfBirth: str
    hasDeclaredBankruptcy: bool
    educationalAttainment: str
    completedCourses: str
    businessName: str
    notes: str
    authorisedRepresentativeNumber: str
    xplanId: int