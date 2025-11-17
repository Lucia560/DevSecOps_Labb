from fastapi import APIRouter, HTTPException, Depends
from app.validation import Item
from app.auth import auth_required

router = APIRouter()

items = {}

@router.get("/")
def root():
    return {"message": "API is working!"}

@router.post("/items", dependencies=[Depends(auth_required)])
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.id] = item
    return {"message": "Item created", "item": item}

@router.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@router.delete("/items/{item_id}", dependencies=[Depends(auth_required)])
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}
