from fastapi import APIRouter
from usecase import person_usecases
from core.person import PersonModel

router = APIRouter(
    prefix="/api/person",
    tags=["Person"],
    responses={404: {"message": "Bad Request"},
               500: {"message": "Internal Server Error"}},
    redirect_slashes=True,
)


@router.get("/{personId}",
            summary="Retrieve a person",
            description=("Get a person from the database by their ID. "),
            response_model=PersonModel,
            )
def retrieve_person(personId: str):
    return person_usecases.get_person(personId)

@router.get("/",
            summary="Retrieve all persons",
            description=("Get all people in the database."),
            response_model=list[PersonModel],
            )
def retrieve_people():
    return person_usecases.get_people()


@router.post("/",
             summary="Create a person",
             description=("Create a person in the database."),
             response_model=PersonModel,
             )
def create_person(person: PersonModel):
    return person_usecases.create_person(person)


@router.put("/{personId}",
            summary="Update a person",
            description=("Update a person in the database. "),
            response_model=PersonModel,
            )
def update_person(personId: str, person: PersonModel):
    return person_usecases.update_person(personId, person)


@router.delete("/{personId}",
                summary="Delete a person",
                description=("Delete a person from the database. "),
                response_model=dict,
                )
def delete_person(personId: str):
    return person_usecases.delete_person(personId)