from fastapi import APIRouter
from app.database.connection import db
from bson import ObjectId
import math


router = APIRouter()

def clean_value(value):
    if isinstance(value, float):
        if math.isinf(value) or math.isnan(value):
            return None
    return value

def serialize_mcq(mcq):
    return {
        "id": str(mcq["_id"]),
        "sno": clean_value(mcq.get("sno")),
        "question": clean_value(mcq.get("question")),
        "optionA": clean_value(mcq.get("optionA")),
        "optionB": clean_value(mcq.get("optionB")),
        "optionC": clean_value(mcq.get("optionC")),
        "optionD": clean_value(mcq.get("optionD")),
        "correctoption": clean_value(mcq.get("correctAnswer")),
        "section": clean_value(mcq.get("section")),
    }

@router.get("/mcqs")
async def get_mcqs():
    raw_mcqs = await db.mcqs.find().to_list(length=100)
    return [serialize_mcq(mcq) for mcq in raw_mcqs]