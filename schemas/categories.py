from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    id: int
    name: str = Field()

class CategoryCreate(BaseModel):
    name: str = Field()