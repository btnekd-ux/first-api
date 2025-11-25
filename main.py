from typing import Annotated
from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, EmailStr
import uvicorn # type: ignore

app = FastAPI()

class createUser(BaseModel):
    emeil: EmailStr
    
    

@app.get("/")
def hello_index():
    return {
        "message": "Hello, index!"
    }
    
    
@app.get("/hello/")
def hello(name: str):
    name = name.strip.title()
    return {"message": f"Hello, {name}!"}


@app.get("/users/")
def create_user(user: createUser):
    return{ 
        "message": "success",
        "email": user.email,
    }
    
    
    
@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        a: a,
        b: b,
        "result": a + b,
    }   
    

    
@app.get("/item/")
def list_items():
    return [
        "item1",
        "item2",
    ]
    
    
@app.get("/item/{item_id}/")    
def get_item_by_id(item_id: int):
    return{
        "id":item_id,
    }

#Automatically reload the server on code changes
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)