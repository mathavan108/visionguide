import cv2
import time


class Camera:
    def __init__(self, camera_index=0):
        """
        Initialize the webcam.
        camera_index = 0 means the default webcam.
        """
        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            raise Exception("Error: Unable to access webcam.")

    def get_frame(self):
        """
        Capture a single frame from the webcam.
        Returns the frame as a NumPy array.
        """
        ret, frame = self.cap.read()

        if not ret:
            return None

        # Resize for faster AI inference
        frame = cv2.resize(frame, (640, 480))

        return frame

    def release(self):
        """
        Release the webcam resource.
        """
        self.cap.release()


def preview_camera():
    """
    Preview the webcam feed.
    Press 'q' to quit.
    """
    camera = Camera()

    while True:
        frame = camera.get_frame()

        if frame is None:
            print("Failed to capture frame.")
            break

        cv2.imshow("VisionGuide Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    preview_camera()