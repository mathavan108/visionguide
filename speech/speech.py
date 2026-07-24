import pyttsx3


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

        # Speech rate
        self.engine.setProperty("rate", 165)

        # Volume
        self.engine.setProperty("volume", 1.0)

    def speak(self, text):
        print("Speaking:", text)
        self.engine.say(text)
        self.engine.runAndWait()