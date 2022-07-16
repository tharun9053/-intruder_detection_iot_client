import time
import cv2


def recordToStream():
    cam = cv2.VideoCapture(0)
    cam.set(3, 320)
    cam.set(4, 240)
    framerate = 10
    currtime = time.time()
    while True:
        ret, frame = cam.read()
        if( (time.time() - currtime) > 1./framerate):
            frame = cv2.imencode('.jpg',frame)[1]
            yield b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n'




if __name__ == '__main__':
    iter = recordToStream()
    next(iter)
    
