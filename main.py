from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

import uvicorn # type: ignore
from items_views import router as items_router


app = FastAPI()
app.include_router(items_router)

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
            


#Automatically reload the server on code changes
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)