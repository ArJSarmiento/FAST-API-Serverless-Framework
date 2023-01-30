import os
from fastapi import FastAPI
from mangum import Mangum
from fastapi.responses import HTMLResponse
from controller import person_controller

STAGE = os.environ.get('STAGE')
root_path = f'/{STAGE}' if STAGE else '/'
app = FastAPI(title="Integration API", root_path=root_path)
    
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

app.include_router(person_controller.router)

# Mangum Handler, this is so important
handler = Mangum(app)