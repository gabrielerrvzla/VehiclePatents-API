from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

# Services
from services import IdServices, PatentServices

router = APIRouter(
    prefix="/id",
    tags=["ID"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=PatentServices)
async def get_patent_code_by_id(id: IdServices = Body(...)):
    return JSONResponse(
        status_code=200,
        content={"patent_code": id.get_patent_code()},
    )
