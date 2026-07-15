from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
import traceback

from orchestrator import analyze

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/analyze")
async def analyze_bug(file: UploadFile = File(...)):
    try:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = analyze(filepath)

        return result

    except Exception as e:
        print("========== BACKEND ERROR ==========")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))