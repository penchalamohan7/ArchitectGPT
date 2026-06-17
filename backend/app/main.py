from fastapi import FastAPI

from app.routes.api_routes import router

app = FastAPI(
    title="ArchitectGPT",
    version="1.0.0"
)

app.include_router(router)