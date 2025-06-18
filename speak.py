import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
engine.setProperty('rate',225)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[3].id)

def say(text):
    engine.say(text)
    engine.runAndWait()