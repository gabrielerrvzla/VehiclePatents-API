from pydantic import BaseModel, Field


class IdSchema(BaseModel):
    id_code: int = Field(
        ...,
        description="ID code",
        example=1,
        min_value=1,
    )
