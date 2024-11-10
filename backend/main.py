from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Audio Overlay Tool"}

@app.post("/overlay")
async def overlay_audio(file: UploadFile = File(...)):
    # Placeholder for file processing
    return JSONResponse(content={"message": "Audio overlay successful"})
