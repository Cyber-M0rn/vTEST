from fastapi import FastAPI

from database import engine
from . import Schemas, Models

app = FastAPI()

Models.Base.metadata.create_all(engine)
@app.post('/User')
def create(request: Schemas.User):
    return request