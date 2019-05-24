import cv2 as cv

cap = cv.VideoCapture("rtsp://192.168.1.2:8080/out.h264")
while(1):
    ret, frame = cap.read()
    cv.imshow('VIDEO', frame)
    cv.waitKey(1)
