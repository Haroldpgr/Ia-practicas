# asistente.py
from reconocimiento_voz import escuchar
from procesamiento_nlp import procesar_pregunta
from conocimientos import buscar_respuesta
from sintesis_voz import hablar
import pyttsx3
from reconocimiento_voz import escuchar
engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

# Base de conocimientos (puede extenderse según sea necesario)
conocimientos = {
    "hola": "¡Hola! Soy tu asistente AI.",
    "aprender": "Soy un ejemplo básico y no tengo la capacidad de aprender de forma continua.",
    "informacion": "No tengo información almacenada actualmente.",
}

def procesar_y_responder(comando):
    comando = comando.lower()

    if comando in conocimientos:
        respuesta = conocimientos[comando]
    else:
        respuesta = "Lo siento, no entiendo ese comando."

    print(f"Procesando y respondiendo a: {comando}")
    print(f"Respuesta: {respuesta}")
    hablar(respuesta)

def main():
    hablar("¡Bienvenido! Soy tu asistente AI. Puedes preguntarme lo que desees.")

    while True:
        comando = escuchar()
        if comando:
            print("Entendí tu pregunta.")
            procesar_y_responder(comando)
        else:
            print("No pude entender tu pregunta. ¿Puedes repetirla?")

if __name__ == "__main__":
    main()
