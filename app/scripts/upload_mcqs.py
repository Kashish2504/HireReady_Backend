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
    collection = db.mcqs

except Exception as e:
    print(f'Error in Connection.py: {e}')
print(type(collection), collection)

async def insert_mcq_data(sno, question, optionA, optionB, optionC, optionD, correctAnswer, section):
    mcq = {
        "sno": int(sno),
        "question": question,
        "optionA": optionA,
        "optionB":optionB,
        "optionC":optionC,
        "optionD":optionD,
        "correctAnswer":correctAnswer,
        "section":section
    }
    await collection.insert_one(mcq)
    print(f"✅ Inserted mcq: {sno} of {section}")

async def upload_mcq_data():
    
    dirpath = "G:\\GitFirst\\HireReady_Backend\\app\\data"
    files = os.listdir(dirpath)
    # print(files)
    for file in files:
        df = pd.read_excel(f"{dirpath}\\{file}")
        print("Start Uploading of File: ", file)
        for index, row in df.iterrows():
            await insert_mcq_data(
                index,
                row['question'],
                row['optionA'],
                row['optionB'],
                row['optionC'],
                row['optionD'],
                row['correctoption'],
                row['section']
            )
        print('All MCQs are uploaded of to mongoDB!')
    print('All Done!')
    


if __name__ == '__main__':
    asyncio.run(upload_mcq_data())