import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Student Loan AI", layout="wide")

st.title("🎓 Student Loan AI System")

tab1, tab2 = st.tabs(["Apply Loan", "Officer Dashboard"])

# ---------------- STUDENT FORM ----------------
with tab1:
    st.header("Student Loan Application")

    name = st.text_input("Student Name")
    parent = st.text_input("Parent Name")
    amount = st.number_input("Loan Amount", min_value=10000)

    if st.button("Submit"):
        res = requests.post(
            "http://localhost:8000/apply-loan/",
            params={"student_name": name, "parent_name": parent, "amount": amount}
        )
        st.success("Loan Submitted Successfully")

# ---------------- OFFICER DASHBOARD ----------------
with tab2:
    st.header("Loan Officer Dashboard")

    res = requests.get("http://localhost:8000/loans/")
    data = res.json()

    df = pd.DataFrame(data, columns=["ID","Student","Parent","Amount","Status","KYC Score"])
    st.dataframe(df)
