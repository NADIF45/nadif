import pyautogui
import cv2
import numpy as np
import time
import threading
from datetime import datetime

SCREEN_SIZE = {"width": 1920, "height": 1080}
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') # type: ignore
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (SCREEN_SIZE["width"], SCREEN_SIZE["height"]))

def screenshot():
    while True:
        img = pyautogui.screenshot()
        img.save(f'screenshot_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')

def record_video():
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frameRGB)

        if cv2.waitKey(1) == ord('q'):
            break

def access_camera():
    cap = cv2.VideoCapture(0)
    out_camera = cv2.VideoWriter('camera_output.avi', fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        out_camera.write(frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    out_camera.release()

def main():
    screenshot_thread = threading.Thread(target=screenshot)
    screenshot_thread.start()

    record_video_thread = threading.Thread(target=record_video)
    record_video_thread.start()

    access_camera_thread = threading.Thread(target=access_camera)
    access_camera_thread.start()

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
