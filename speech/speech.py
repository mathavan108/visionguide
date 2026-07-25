import pyttsx3


class Speaker:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)

        voices = self.engine.getProperty("voices")

        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text):

        if not text:
            return

        print("\n========== SPEAKING ==========")
        print(text)
        print("==============================")

        self.engine.stop()
        self.engine.say(text)
        self.engine.runAndWait()