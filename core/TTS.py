import pyttsx3

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.8)
    
    def say(self, text):
        self.engine.say(text=text)
        
        self.engine.runAndWait()