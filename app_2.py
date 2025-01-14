from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import databases
import sqlalchemy


DATABASE_URL= "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None

@app.on_event("startup")
async def startup():
 await database.connect()


@app.on_event("shutdown")
async def shutdown():
   await database.disconnect()


@app.get("/")
def read_root():
    return {"message": "Hello"}


@app.post("/items/")
async def create_item(item: Item):
   query = items.insert().values(name = item.name, description = item.description)
   last_record_id = await database.execute(query)

   return {**item.dict(), "id": last_record_id}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
   query = items.select().where(items.c.id == item_id)
   item = await database.fetch_one(query)
   if item  is None:
      raise HTTPException(status_code=404, detail="item not found")
   return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    query = items.update().where(items.c.id == item_id).values(name= item.name, description=item.description)
    await database.fetch_one(query)
    return {**item.dict(),"id": item_id}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.fetch_one(query)
    return {"messege","item delete"}
