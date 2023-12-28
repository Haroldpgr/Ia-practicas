import speech_recognition as sr

def escuchar():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=5)  
            print("Di algo...")
            audio = recognizer.listen(source, timeout=10)  
            print("Reconociendo...")
            texto = recognizer.recognize_google(audio)
            print(f"Has dicho: {texto}")
            return texto
    except sr.WaitTimeoutError:
        print("Tiempo de espera agotado. No se detectó ninguna frase. ¿Puedes repetirla?")
        return ""
    except sr.UnknownValueError:
        print("No se pudo entender el audio. ¿Puedes repetir la pregunta?")
        return ""
    except sr.RequestError as e:
        print(f"Error en la solicitud a Google: {e}")
        return ""
