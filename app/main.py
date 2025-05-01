from fastapi import FastAPI
from app.routes import user_routes
from app.database.connection import check_connection, db
import os
import pandas as pd
from app.routes import job_routes, mcq_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:5173",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await check_connection()

app.include_router(user_routes.router, prefix="/api/user", tags=["User"])
app.include_router(job_routes.router, prefix="/api", tags=["Jobs"])
app.include_router(mcq_routes.router, prefix="/api", tags=['MCQs'])


# @app.get("/jobs")
# def dashboard():
#     jobs = db.jobs.find().to_list(length=100)
#     return jobs


    # file_path = "G:\\GitFirst\\HireReady_Backend\\app\\Job_details.xlsx"

    # if not os.path.exists(file_path):
    #     return {"error": "Excel file not found"}

    # try:
    #     data = pd.read_excel(file_path)

    #     print("Excel Columns:", data.columns.tolist())
    #     data = data.fillna("N/A")

    #     job_list = []

    #     for index, row in data.iterrows():
    #         job_list.append({
    #             "id": int(index),
    #             "position": str(row.get("position", "N/A")),
    #             "applyLink": str(row.get("applyLink", "N/A")),
    #             "Company": str(row.get("company", "N/A"))
    #         })

    #     return job_list

    # except Exception as e:
    #     return {"error": str(e)}