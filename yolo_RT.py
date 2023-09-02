import os
import subprocess
import sys

# Verifica si todas las dependencias están instaladas
dependencies = open('requirements.txt').read().splitlines()
for dependency in dependencies:
    try:
        __import__(dependency)
    except ImportError:
        # Si no está instalada, intenta instalarla con pip
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])

# Continúa con el resto de tu código aquí


import cv2
import torch


if torch.cuda.is_available():
    print("La GPU está disponible")
else:
    print("La GPU no está disponible")

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Inference
    results = model(frame)

    # Display the resulting frame with labels
    # cv2.imshow('frame', results.render()[0])

    # Print the objects detected
    for object in results.pandas().xyxy[0]['name'].to_list():
        print(object)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
#cv2.destroyAllWindows()
