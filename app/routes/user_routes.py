from fastapi import APIRouter, HTTPException
from app.models.user_model import User, UserLogin
from app.database.connection import db
from app.utils.auth import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
async def register_user(user: User):
    existing = await db.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user.password = hash_password(user.password)
    result = await db.users.insert_one(user.dict())
    return {"message": "User registered successfully", "id": str(result.inserted_id)}

@router.post("/login")
async def login_user(user: UserLogin):
    existing = await db.users.find_one({"email": user.email})
    if not existing:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(user.password, existing["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"user_id": str(existing["_id"]), "email": existing["email"]})
    return {"access_token": token, "token_type": "bearer"}
