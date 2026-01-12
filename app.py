import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Loan AI", layout="wide")
st.title("🎓 Student Loan AI System")

# ---- Temporary in-memory storage ----
if "loans" not in st.session_state:
    st.session_state.loans = []

tab1, tab2 = st.tabs(["Apply Loan", "Officer Dashboard"])

# -------- STUDENT FORM --------
with tab1:
    st.subheader("Student Loan Application")

    student = st.text_input("Student Name")
    parent = st.text_input("Parent Name")
    amount = st.number_input("Loan Amount", min_value=10000)

    if st.button("Submit Application"):
        if student and parent:
            st.session_state.loans.append({
                "Student": student,
                "Parent": parent,
                "Amount": amount,
                "Status": "Submitted",
                "KYC Score": 0
            })
            st.success("Loan application submitted")
        else:
            st.warning("Please fill all details")

# -------- OFFICER DASHBOARD --------
with tab2:
    st.subheader("Loan Officer Dashboard")

    if st.session_state.loans:
        df = pd.DataFrame(st.session_state.loans)
        st.dataframe(df)

        index = st.selectbox("Select Application", df.index)

        if st.button("Verify KYC"):
            st.session_state.loans[index]["KYC Score"] = 85
            st.session_state.loans[index]["Status"] = "KYC Verified"
            st.success("KYC verified")

        if st.button("Approve Loan"):
            st.session_state.loans[index]["Status"] = "Approved"
            st.success("Loan approved")

        if st.button("Reject Loan"):
            st.session_state.loans[index]["Status"] = "Rejected"
            st.error("Loan rejected")
    else:
        st.info("No loan applications yet")
