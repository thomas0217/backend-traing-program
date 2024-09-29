from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name: str ="Test Item"
    description: str ="A test description"
    price: float = 10.5
    tax: float = 1.5

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put("/items/{item_id}")
async def read_item(item_id: int, item: Item, q : str | None = None):
    results={"item_id" : item_id,"name": item.name, "description": item.description,
             "price" : item.price, "tax" : item.tax}
    if q:
        results.update({"q":q})
    return results 
#frfafd