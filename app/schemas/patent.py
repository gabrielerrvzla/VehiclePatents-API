from pydantic import BaseModel, Field

class PatentSchema(BaseModel):
    patent_code: str = Field(
        ...,
        description="Patent code",
        example="AAAA000",
        min_length=7,
        max_length=7,
        regex="^[A-Z]{4}[0-9]{3}$",
    )
