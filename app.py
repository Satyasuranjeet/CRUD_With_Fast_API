from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allows all headers
)
client = MongoClient(MONGO_URL)
db=client["Fast_API-CRUD"]
collection=db["Item"]

class Item(BaseModel):
    name:str
    details:str
    price:float

def item_with_id(item):
    return {**item, "_id": str(item["_id"])}

@app.post("/item/")
async def create(item:Item):
    tem=item.dict()
    a=collection.insert_one(tem)
    created_item = collection.find_one({"_id": a.inserted_id})  # Fetch inserted item
    return item_with_id(created_item)
@app.get("/item/")
async def print():
    item=collection.find()
    return [ item_with_id(i) for i in item]
@app.get("/item/name/{name}")
async def find(name):
    a=collection.find_one({"name":name})
    if not a :
        raise HTTPException(status_code=404,details="Item Not Found")
    return item_with_id(a)

@app.put("/item/update/{name}")
async def update(name: str, item: Item):
    existing_item = collection.find_one({"name": name})
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item Not Found")

    collection.update_one({"name": name}, {"$set": item.dict()})
    updated_item = collection.find_one({"name": name})  # Fetch updated item
    return item_with_id(updated_item)

@app.delete("/item/{name}")
async def delete(name: str):
    item = collection.find_one({"name": name})
    if not item:
        raise HTTPException(status_code=404, detail="Item Not Found")

    collection.delete_one({"name": name})
    return {"message": f"Item '{name}' deleted successfully"}   