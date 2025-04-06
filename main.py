from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import motor.motor_asyncio
import re
def is_safe_string(input_str: str) -> bool:
    return not bool(re.search(r"[\$\{\}]", input_str))


app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://admin:LEAFclover404@de-cluster.s1uaq.mongodb.net/?retryWrites=true&w=majority&appName=DE-cluster"
)
db = client.multimedia_db

class PlayerScore(BaseModel):
    player_name: str
    score: int

@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    content = (await file.read()).decode("latin1")
    sprite_doc = {"filename": file.filename, "content": content}
    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}

@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    content = (await file.read()).decode("latin1")
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}

from fastapi import HTTPException
@app.post("/player_score")
async def add_score(score: PlayerScore):
    if not is_safe_string(score.player_name):
        raise HTTPException(status_code=400, detail="Invalid characters in player name")

    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}

