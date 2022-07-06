from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

# Services
from services import PatentServices, IdServices

router = APIRouter(
    prefix="/patent",
    tags=["Patent"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=IdServices)
async def get_id_by_patent_code(patent: PatentServices = Body(...)):
    return JSONResponse(
        status_code=200,
        content={"id_code": patent.get_id()},
    )
