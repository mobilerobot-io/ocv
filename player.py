import numpy as np
import cv2 as cv

def must_get_cam():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: failed to open cam")
        exit()
    return cap

cap = must_get_cam()

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("ERROR: can not recv any frames")
        break

    frame = cv.flip(frame, 0)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # save the image
    out.write(gray)

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()

