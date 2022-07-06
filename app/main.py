from fastapi import FastAPI
from routers import id_router, patent_router

# FastAPI App
app = FastAPI(
    title="Vehicle patents",
    description="REST API to generate and verify vehicle license plates",
    version="1.0.0",
)

# Routes
app.include_router(prefix="/api/v1", router=id_router)
app.include_router(prefix="/api/v1", router=patent_router)