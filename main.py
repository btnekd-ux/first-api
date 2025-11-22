from fastapi import FastAPI
import uvicorn # type: ignore

app = FastAPI()

@app.get("/")
def hello_index():
    return {
        "message": "Hello, index!"
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