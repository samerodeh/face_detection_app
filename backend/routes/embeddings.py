from fastapi import APIRouter, UploadFile, File
import shutil
import numpy as np
import os

from utils import face
from models.schemas import UserEmbeddings
from utils.face import get_embedding, cosine_similarity
from db.db import insert_embedding, delete_embedding as db_delete_embedding, embedding_exists


router = APIRouter()


@router.post("/create-embedding")
async def get_face_embedding(file: UploadFile = File(...), name: str = "unknown"):
    os.makedirs("temp_images", exist_ok=True)  
    temp_path = f"temp_images/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    embedding = get_embedding(temp_path)
    if embedding is None:
        return {"success": False, "message": "No face detected"}

    # Check if embedding for this person_name already exists
    if embedding_exists(name):
        return {"success": False, "message": f"Embedding for {name} already exists"}

    # Save embedding to DB
    insert_embedding(name, embedding)

    return {"success": True, "embedding": embedding, "message": f"Embedding saved for {name}"}




@router.delete('/delete-embedding')
def delete_embedding(person_name: str):
    try:
        db_delete_embedding(person_name)
        return {"success": True, "message": f"Embedding deleted for {person_name}"}
    except Exception as e:
        return {"success": False, "error": str(e)}
    

@router.put('/update-embedding')
def update_embedding(person_name: str, new_person_name: str):
        try:
            update_embedding(person_name, new_person_name)
            return {"success": True, "message": f"Embedding updated for {person_name}"}
        except Exception as e:
            return {"success": False, "error": str(e)}
        

@router.post("/compare-faces")
async def compare_faces(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    path1, path2 = f"temp/{file1.filename}", f"temp/{file2.filename}"
    with open(path1, "wb") as f: shutil.copyfileobj(file1.file, f)
    with open(path2, "wb") as f: shutil.copyfileobj(file2.file, f)

    emb1 = get_embedding(path1)
    emb2 = get_embedding(path2)

    if not emb1 or not emb2:
        return {"match": False, "message": "Face not detected"}

    score = cosine_similarity(np.array(emb1), np.array(emb2))
    return {"match": score > 0.3, "similarity": score}