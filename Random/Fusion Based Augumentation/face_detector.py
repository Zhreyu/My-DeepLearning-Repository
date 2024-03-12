import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()

def detect_face_and_resize(image_path):
    image = cv2.imread(image_path)
    detected_faces = detector.detect_faces(image)
    if detected_faces:
        x, y, w, h = detected_faces[0]['box']
        face = image[y:y+h, x:x+w]
        resized_face = cv2.resize(face, (224, 224))
        return resized_face
    return cv2.resize(image,(224,224))
