from deepface import DeepFace

def verify_face(img1, img2):
    try:
        result = DeepFace.verify(img1, img2, enforce_detection=False)
        return result["verified"], result["distance"]
    except Exception as e:
        return False, 1.0
