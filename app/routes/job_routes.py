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

def serialize_job(job):
    return {
        "id": str(job["_id"]),
        "sno": clean_value(job.get("sno")),
        "position": clean_value(job.get("position")),
        "applyLink": clean_value(job.get("applyLink")),
        "company": clean_value(job.get("company")),
    }

@router.get("/jobs")
async def get_jobs():
    raw_jobs = await db.jobs.find().to_list(length=100)
    jobs = [serialize_job(job) for job in raw_jobs]
    return jobs