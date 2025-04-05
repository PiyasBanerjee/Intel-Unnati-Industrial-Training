# main.py
import cv2
from recognizer import load_known_faces, recognize_face
from utils import speak
from voice_command import listen_for_update
from display import get_customer_data

known_encodings, known_names = load_known_faces()

cap = cv2.VideoCapture(0)
detected = set()

while True:
    ret, frame = cap.read()
    name, face = recognize_face(frame, known_encodings, known_names)

    if name and name not in detected:
        speak(f"Welcome {name}")
        print("Waiting for 'update' command...")
        if listen_for_update():
            data = get_customer_data(name)
            print(f"Customer Data for {name}: {data}")
        detected.add(name)

    cv2.imshow("Customer Face Recognition", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
