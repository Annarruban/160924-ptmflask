from pydantic import BaseModel, Field, ConfigDict


class CategoryBase(BaseModel):
    id: int
    name: str


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=10) # ... = required
    category_id: int = Field(gt=0)


class QuestionResponse(BaseModel):
    id: int
    text: str
    category: CategoryBase
    category_id: int | None = None

    model_config = ConfigDict(
        from_attributes = True
    )

