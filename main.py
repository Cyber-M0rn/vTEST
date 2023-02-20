from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
@app.get('/user/')
def User(limit=10,published: bool=True, sort: Optional[str]=None):
    if published:
        return{'data': f'{limit}published blog list from db'}
    else:
        return {'data': f'{limit}all blog list from db'}
def unpublised():
    return {'data': 'all unpublished blogs'}

@app.post('/user/')
def create_blog():
    return {'data': "Blog is create"}


@app.delete('/User/{ID}')
async def delete_item(item_id:int, q: str=None):
    from http.client import HTTPException
    raise HTTPException(status_code=404, detail="Item not found")
    delete_item_from_db(item_id)
    return {"message": "Item deleted"}
class User(BaseModel):
    title :str
    body: str
    publised: Optional[bool]
@app.get('By {ID}')
def user_id(id,limit=10):
    return{'message': {'1,2,3,4,5'}}

@app.put('/user/{ID}')
def update(user: User):
    username=user.username
    user.db[username]=user_id.dict()
    return {'data': f'Successfully updated user: {username}'}
