from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., min_length=1, example="Laptop")
    price: float = Field(..., gt=0, example=999.99)
