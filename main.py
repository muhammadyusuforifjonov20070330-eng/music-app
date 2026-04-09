from fastapi import FastAPI, UploadFile, File
from sxema import save_file
from fastapi.responses import FileResponse
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Musiqa eshitaylik", docs_url='/')

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    return save_file(file)

@app.get("/fayl_korish/{filename}")
def fayl_korish(filename: str):
    path = f"audio/{filename}"
    if not os.path.exists(path):
        return {"error": "Fayl topilmadi"}
    return FileResponse(path, media_type="audio/mpeg")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
