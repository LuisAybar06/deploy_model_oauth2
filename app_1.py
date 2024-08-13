from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_db = {
    1: {"name": "Item 1", "description": "This is the item 1"},
    2: {"name": "Item 2", "description": "This is the item 2"}
}

@app.get("/")
def read_root():
    return {"message": "Hello"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in fake_db:
        return fake_db[item_id]
    else:
        raise HTTPException(status_code=404, detail="item not found")
    
@app.post("/items/")
def create_item(item_id, name: str, description: str):
    if item_id in fake_db:
        raise HTTPException(status_code=400, detail="item ya existe")
    
    fake_db[item_id] = {"name": name, "description": description}
    return fake_db[item_id]