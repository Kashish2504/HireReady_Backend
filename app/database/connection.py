import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

uri = "mongodb+srv://admin:Admin%400053@cluster0.uks5i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    async def check_connection():
        try:
            await client.admin.command("ping")
            print("DB connected!")
        except:
            print("Connection Failed!")

    db = client.HireReady

except Exception as e:
    print(f'Error in Connection.py: {e}')
