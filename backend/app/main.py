from fastapi import FastAPI, UploadFile, File
from app.services.openapi_parser import parse_openapi
from app.services.storage_service import save_api, load_api, set_current_api, get_current_api
from app.models.chat_request import ChatRequest

from app.services.prompt_service import build_prompt

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
    set_current_api(file.filename)

    return {
    "message": "Uploaded successfully",
    "parsed": parsed
    }

@app.get("/summary")
def get_summary():

    current = get_current_api()
    data = load_api(current)

    return data

@app.post("/chat")
def chat(request: ChatRequest):

    data = load_api(get_current_api())

    prompt = build_prompt(data, request.question)

    return {
        "prompt": prompt
    }