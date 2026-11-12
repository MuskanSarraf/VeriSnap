

import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    X = []
    y = []


    student_db = get_all_students()

    if not student_db:
        return None
    
    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))

    if len(X) == 0:
        return 0
    
    clf = SVC(kernel='linear', probability=True, class_weight='balanced')

    try:
        clf.fit(X, y)
    except ValueError:
        pass

    return {'clf': clf, 'X':X, "y":y}


def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)




def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected_student = {}

    if not encodings:
        return detected_student, [], 0

    all_students = get_all_students() or []

    # Keep only students with valid 128-dimensional embeddings.
    students_with_embeddings = []

    for student in all_students:
        embedding = student.get("face_embedding")

        if embedding is None:
            continue

        try:
            embedding = np.asarray(embedding, dtype=np.float64)
        except (TypeError, ValueError):
            continue

        if embedding.shape != (128,) or not np.all(np.isfinite(embedding)):
            continue

        students_with_embeddings.append((student["student_id"], embedding))

    all_ids = [student_id for student_id, _ in students_with_embeddings]

    if not students_with_embeddings:
        return detected_student, all_ids, len(encodings)

    # Temporary conservative threshold; validate with test images.
    resemblance_threshold = 0.40

    for encoding in encodings:
        encoding = np.asarray(encoding, dtype=np.float64)

        if encoding.shape != (128,) or not np.all(np.isfinite(encoding)):
            continue

        distances = [
            (
                student_id,
                float(np.linalg.norm(stored_embedding - encoding))
            )
            for student_id, stored_embedding in students_with_embeddings
        ]

        best_student_id, best_distance = min(
            distances, key=lambda item: item[1]
        )

        print("Face matching results:")
        for student_id, distance in distances:
            print(f"  Student {student_id}: {distance:.4f}")

        print(
            f"Closest student: {best_student_id}, "
            f"distance: {best_distance:.4f}"
        )

        if best_distance <= resemblance_threshold:
            detected_student[best_student_id] = True
        else:
            print("Unknown face: registration should be offered.")

    return detected_student, all_ids, len(encodings)
