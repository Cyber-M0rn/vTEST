from pydantic import BaseModel

class User(BaseModel):
    title: str
    body: str