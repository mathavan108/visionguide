import cv2
import time
import os


class Camera:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            raise Exception("Unable to open webcam.")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def get_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            return None

        return frame

    def save_frame(self, frame, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        cv2.imwrite(path, frame)

    def release(self):
        self.cap.release()


def live_preview():

    camera = Camera()

    last_capture = time.time()

    capture_interval = 2      # seconds

    while True:

        frame = camera.get_frame()

        if frame is None:
            break

        cv2.imshow("VisionGuide Live Camera", frame)

        current_time = time.time()

        if current_time - last_capture >= capture_interval:

            camera.save_frame(frame, "assets/images/live.jpg")

            print("Frame Captured")

            last_capture = current_time

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    live_preview()