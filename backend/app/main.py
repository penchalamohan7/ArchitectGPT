from fastapi import FastAPI, UploadFile, File
from app.services.openapi_parser import parse_openapi
from app.services.storage_service import save_api
import os
import shutil

app = FastAPI(
    title="ArchitectGPT",
    version="1.0.0"
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Welcome to ArchitectGPT"
    }

@app.post("/upload")
async def upload_api(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    parsed = parse_openapi(filepath)

    save_api(file.filename, parsed)

    return {
    "message": "Uploaded successfully",
    "parsed": parsed
    }