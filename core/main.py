import os
from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import HTMLResponse, JSONResponse
from core.exception.person import PersonNotFoundError, InvalidPersonError, PersonConflictError
from controller.person_controller import router

STAGE = os.environ.get('STAGE')
root_path = f'/{STAGE}' if STAGE else '/'
app = FastAPI(
    root_path=root_path,
    title="Integration API", 
    contact={
        "name": "Arnel Jan Sarmiento",
        "email": "rneljan@gmail.com",
    },
)

#Person exception
@app.exception_handler(PersonNotFoundError)
async def person_not_found_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(PersonConflictError)
async def person_conflict_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

@app.exception_handler(InvalidPersonError)
async def person_status_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# root url
@app.get("/", include_in_schema=False)
def welcome():
    html_content = """
    <html>
        <head>
            <title>Welcome to the Integration API</title>
        </head>
        <body>
            <h1>Welcome to the Integration API</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# Person Controller
app.include_router(router)

# Mangum Handler, this is so important
handler = Mangum(app)