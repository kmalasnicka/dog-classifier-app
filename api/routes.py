from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from services.image_processor import ImageProcessor
from utils.logger import setup_logger

image_router = APIRouter(prefix="/api/v1",tags=["image_classification"])
logger = setup_logger()

@image_router.post("/predict",response_model=dict)
async def predict_image(file: UploadFile = File(...)):
    try:
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code = 400, detail="Uploaded file is not image")
        content = await file.read()

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "size_bytes": len(content)
        }
    except Exception as e:
        raise HTTPException(status_code = 500,detail=f"Error: {str(e)}")
    