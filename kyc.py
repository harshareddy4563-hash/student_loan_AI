from ml.face_verification import verify_face
from ml.ocr import extract_text

def perform_kyc(face_live, face_id, document):
    face_verified, distance = verify_face(face_live, face_id)
    doc_text = extract_text(document)

    score = 0
    if face_verified:
        score += 60
    if len(doc_text) > 20:
        score += 40

    return {
        "face_verified": face_verified,
        "kyc_score": score,
        "document_text": doc_text
    }
