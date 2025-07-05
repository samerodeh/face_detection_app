# fastapi imports

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os

# files imports

from db import db
from routes import embeddings, auth
from utils import face

app = FastAPI(
    title="Face Detection API",
    description="API for face detection and user authentication",
    version="1.0.0"
)

# Include routers
app.include_router(auth.router)
app.include_router(embeddings.router)



# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
def upload_image(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    contents = file.file.read()
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(contents)
    return JSONResponse(content={"message": f"✅ {file.filename} received successfully"})








