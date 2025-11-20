from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int = Field(...)
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Laptop",
                    "price": 999.99
                }
            ]
        }
    }

