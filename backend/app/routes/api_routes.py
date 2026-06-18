import os
import shutil

from fastapi import APIRouter, UploadFile, File
from app.services.review_storage_service import load_reviews
from app.models.chat_request import ChatRequest
from app.services.review_service import review_api
from app.services.openapi_parser import parse_openapi
from app.services.storage_service import (
    save_api,
    load_api,
    set_current_api,
    get_current_api
)

from app.services.prompt_service import build_prompt
from app.services.llm_service import ask_llm
from app.services.codegen_service import generate_spring_controller
from app.services.angular_codegen_service import generate_angular_service


router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.get("/")
def home():
    return {
        "status": "running",
        "message": "Welcome to ArchitectGPT 🚀"
    }


@router.post("/upload")
async def upload_api(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    parsed = parse_openapi(filepath)

    save_api(file.filename, parsed)

    set_current_api(file.filename)

    return {
        "message": "Uploaded Successfully",
        "parsed": parsed
    }


@router.get("/summary")
def get_summary():

    current = get_current_api()

    data = load_api(current)

    return data


@router.post("/chat")
def chat(request: ChatRequest):

    current = get_current_api()

    data = load_api(current)

    prompt = build_prompt(data, request.question)

    answer = ask_llm(prompt)

    return {
        "answer": answer
    }

@router.get("/review")
def review():

    summary = load_api(get_current_api())

    return review_api(summary)

@router.get("/reviews")

def reviews():

    return load_reviews()

@router.get("/generate/spring")

def generate():

    summary = load_api(get_current_api())

    code = generate_spring_controller(summary)

    return {

        "language": "Spring Boot",

        "code": code

    }

@router.get("/generate/angular")
def generate_angular():

    summary = load_api(get_current_api())

    return {
        "language": "Angular",
        "code": generate_angular_service(summary)
    }