from fastapi import FastAPI
import sqlite3
from backend.kyc import perform_kyc

app = FastAPI()

conn = sqlite3.connect("database/loans.db", check_same_thread=False)
cursor = conn.cursor()

@app.post("/apply-loan/")
def apply_loan(student_name: str, parent_name: str, amount: int):
    cursor.execute(
        "INSERT INTO loans VALUES (NULL,?,?,?, 'Submitted', 0)",
        (student_name, parent_name, amount)
    )
    conn.commit()
    return {"message": "Loan application submitted"}

@app.get("/loans/")
def get_loans():
    cursor.execute("SELECT * FROM loans")
    return cursor.fetchall()

@app.post("/kyc/")
def kyc():
    result = perform_kyc(
        "sample_images/live.jpg",
        "sample_images/id.jpg",
        "sample_images/doc.jpg"
    )
    return result
