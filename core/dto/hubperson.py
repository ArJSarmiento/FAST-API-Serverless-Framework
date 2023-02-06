from pydantic import BaseModel


class HubPersonDTO(BaseModel):
    entryId: str
    entryStatus: str
    createDate: str
    updateDate: str
    createdBy: str
    updatedBy: str
    userGroup: str
    userRoles: list[str]
    firstName: str
    lastName: str
    practiceId:str