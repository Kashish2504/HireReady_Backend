import motor.motor_asyncio
import os
from dotenv import load_dotenv
import pandas as pd
import asyncio

load_dotenv()

uri = "mongodb+srv://admin:Admin%400053@cluster0.uks5i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
collection = 0
try:
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    async def check_connection():
        try:
            await client.admin.command("ping")
            print("DB connected!")
        except:
            print("Connection Failed!")

    db = client.HireReady
    collection = db.jobs


except Exception as e:
    print(f'Error in Connection.py: {e}')
print(type(collection), collection)

async def insert_job_record(sno, position, applyLink, company):
    job = {
        "sno": int(sno),
        "position": position,
        "applyLink": applyLink,
        "company": company
    }
    await collection.insert_one(job)
    print(f"✅ Inserted job: {position} at {company}")

async def upload_jod_data():
    file_path = "G:\\GitFirst\\HireReady_Backend\\app\\Job_details.xlsx"
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        await insert_job_record(
            index,
            row['position'],
            row['applyLink'],
            row['company']
        )
    print('All Jobs are Uploaded to MongoDB!')

if __name__ == '__main__':
    asyncio.run(upload_jod_data())
