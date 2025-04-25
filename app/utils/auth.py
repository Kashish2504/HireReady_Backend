import bcrypt
import jwt
from datetime import datetime, timedelta
import os

# SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")  # keep secret in env in prod
SECRET_KEY = "sjfglasjkfg"
ALGORITHM = "HS256"

# Password hashing
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Password verification
def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# JWT creation
def create_access_token(data: dict, expires_delta: timedelta = timedelta(days=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
