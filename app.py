import gradio as gr
from face_verification import verify_face
from kyc import perform_kyc
from ocr import read_document

def loan_application(student_name, loan_amount, student_face, parent_face, document):
    face_result = verify_face(student_face, parent_face)
    kyc_score = perform_kyc()
    doc_result = read_document(document)

    return (
        f"Application Submitted ✅\n\n"
        f"Student: {student_name}\n"
        f"Loan Amount: ₹{loan_amount}\n\n"
        f"Face Verification: {face_result}\n"
        f"Document Verification: {doc_result}\n"
        f"KYC Score: {kyc_score}\n\n"
        f"Status: Under Review"
    )

app = gr.Interface(
    fn=loan_application,
    inputs=[
        gr.Textbox(label="Student Name"),
        gr.Number(label="Loan Amount"),
        gr.Image(label="Student Face"),
        gr.Image(label="Parent Face (Surety)"),
        gr.File(label="ID Document")
    ],
    outputs=gr.Textbox(label="Result"),
    title="🎓 Student Loan AI System",
    description="AI-based KYC, Face Verification & Parent Surety (Demo)"
)

app.launch()
