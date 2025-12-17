from fastapi import APIRouter, UploadFile, File
from app.schemas import GenerateRequest, JobResponse
import uuid
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-image")
def upload_image(file :UploadFile = File(...)):
    
    if not file.content_type.startswith("image/"):
        return {"error": "Invalid file type. Please upload an image."}
    
    file_ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"message": "Image uploaded successfully", "filename": filename}