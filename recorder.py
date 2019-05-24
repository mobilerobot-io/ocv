import socket
import subprocess

import numpy as np
import cv2 as cv

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
# server_socket = socket.socket()
# server_socket.bind(('0.0.0.0', 8000))
# server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
# print("Waiting for connection")
# connection = server_socket.accept()[0].makefile('rb')
# print("     got connection")

# Capture cap = new Capture ("udp://@212.1.1.1:1234");
# cap = cv.VideoCapture(connection)
cap = cv.VideoCapture("udp://@225.1.1.1:8000");
try:
    # Run a viewer with an appropriate command line. Uncomment the mplayer
    # version if you would prefer to use mplayer instead of VLC
    # cmdline = ['vlc', '--demux', 'h264', '-']
    # cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
    # player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
    while True:

        ret, frame = cap.read()
        if not ret:
            print("ERROR reading frame")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
        # Repeatedly read 1k of data from the connection and write it to
        # the media player's stdin
        # data = connection.read(1024)
        # if not data:
            # break
        # print("Got data len "+ str(len(data)))
        # player.stdin.write(data)
finally:
    # connection.close()
    # server_socket.close()
    cap.release()
    cv.destroyAllWindows()
        
        
        
