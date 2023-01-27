import os
from fastapi import FastAPI
from mangum import Mangum

STAGE = os.environ.get('STAGE')
root_path = f'/{STAGE}' if STAGE else '/'
app = FastAPI(title="Integration API", root_path=root_path)
@app.get('/hello')
def hello_api(name: str = "World"):
    return {"hello": name}
# Mangum Handler, this is so important
handler = Mangum(app)