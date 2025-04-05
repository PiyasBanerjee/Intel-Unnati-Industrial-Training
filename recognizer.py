# recognizer.py
import face_recognition
import cv2
import os

def load_known_faces(path='data'):
    known_encodings = []
    names = []

    for file in os.listdir(path):
        img = face_recognition.load_image_file(os.path.join(path, file))
        encodings = face_recognition.face_encodings(img)
        if encodings:
            known_encodings.append(encodings[0])
            names.append(os.path.splitext(file)[0])
    return known_encodings, names

def recognize_face(frame, known_encodings, known_names):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding, face in zip(encodings, faces):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        if True in matches:
            index = matches.index(True)
            name = known_names[index]
        return name, face
    return None, None
