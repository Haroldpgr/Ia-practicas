# sintesis_voz.py
import pyttsx3

def hablar(respuesta):
    engine = pyttsx3.init()
    engine.say(respuesta)
    engine.runAndWait()
