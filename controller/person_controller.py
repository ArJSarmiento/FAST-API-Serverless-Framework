from fastapi import APIRouter, Depends
from starlette import status
from core.dto.response import PersonResponse
from core.dto.person import PersonDTO
from usecase.command import CommandUseCase
from usecase.retrieve import RetrieveUseCase

router = APIRouter(
    prefix="/api/person",
    tags=["Person"],
    redirect_slashes=True,
)


@router.get(
    "/{personId}",
    summary="Retrieve a person",
    description=("Get a person from the database by their ID."),
    response_model=PersonResponse,
)
async def retrieve_person(personId: str, retrieve_usecase: RetrieveUseCase = Depends(RetrieveUseCase)):
    return retrieve_usecase.get_person(personId)


@router.get(
    "/",
    summary="Retrieve all persons",
    description=("Get all people in the database."),
    response_model=list[PersonResponse],
)
async def retrieve_people(retrieve_usecase: RetrieveUseCase = Depends(RetrieveUseCase)):
    return retrieve_usecase.get_people()

@router.post(
    "/",
    summary="Create a person",
    description=("Create a person in the database."),
    response_model=PersonResponse,
)
async def create_person(person: PersonDTO, command_usecase: CommandUseCase = Depends(CommandUseCase)):
    person = command_usecase.create_person(person)
    return PersonResponse.build_result(person)


@router.patch(
    "/{personId}",
    summary="Update a person",
    description=("Update a person in the database."),
    response_model=PersonDTO,
)
async def update_person(personId: str, person: PersonDTO, command_usecase: CommandUseCase = Depends(CommandUseCase)):
    person = command_usecase.update_person(personId, person)
    return person
    # return PersonResponse.build_result(person)


@router.delete(
    "/{personId}",
    summary="Delete a person",
    description=("Delete a person from the database."),
    response_model=PersonDTO,
)
async def delete_person(personId: str, command_usecase: CommandUseCase = Depends(CommandUseCase)):
    person = command_usecase.delete_person(personId)
    return person
    # return PersonResponse.build_result(person)
