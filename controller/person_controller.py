# PersonController is a controller that handles all requests to the /api/person endpoint
from fastapi import APIRouter

from core.dto.response import PersonOut, HubPersonOut
from core.dto.request import PersonIn
from core.dto.error_response import ServerError, PersonNotFoundError

from usecase.command import CommandUseCase
from usecase.retrieve import RetrieveUseCase

from repository.person_repository import PersonRepository
from data_store.person_dynamodb import PersonDynamoDB
from external_gateway.auth_service import Auth


auth = Auth()
person_dynamodb = PersonDynamoDB("integration-person-arnel")
person_repository = PersonRepository(person_dynamodb)
retrieve_usecase = RetrieveUseCase(auth)
command_usecase = CommandUseCase(person_repository, auth)

router = APIRouter(
    prefix="/api/person",
    tags=["Person"],
    redirect_slashes=True,
    responses={
        500: {"model": ServerError},
    }
)


@router.get(
    "/{entryId}",
    summary="Retrieve a person",
    description="Get a person from the database by their ID.",
    response_model=HubPersonOut,
    responses={
        404: {"model": PersonNotFoundError}
    },
)
async def retrieve_person(entryId: str, practice_id: str = None):
    person = await retrieve_usecase.get_person(entryId, practice_id)
    return HubPersonOut.build_result(person)


@router.get(
    "/",
    summary="Retrieve all persons",
    description="Get all people in the database.",
    response_model=list[HubPersonOut],
)
async def retrieve_people():
    people = await retrieve_usecase.get_people()
    return [HubPersonOut.build_result(person) for person in people]


@router.post(
    "/",
    summary="Create a person",
    description="Create a person in the database.",
    response_model=PersonOut,
)
async def create_person(person: PersonIn):
    person = await command_usecase.create_person(person)
    return PersonOut.build_result(person)


@router.patch(
    "/{entryId}",
    summary="Update a person",
    description="Update a person in the database.",
    response_model=PersonOut,
    responses={
        404: {"model": PersonNotFoundError}
    },
)
async def update_person(entryId: str, practiceId:str, person: PersonIn):
    person = await command_usecase.update_person(entryId, practiceId, person)
    return PersonOut.build_result(person)


@router.delete(
    "/{entryId}",
    summary="Delete a person",
    description="Delete a person from the database.",
    response_model=PersonOut,
    responses={
        404: {"model": PersonNotFoundError}
    },
)
async def delete_person(entryId: str, practiceId: str = None):
    person = await command_usecase.delete_person(entryId, practiceId)
    return PersonOut.build_result(person)
