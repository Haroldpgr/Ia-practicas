# conocimientos.py
import pandas as pd
def cargar_conocimientos():
    # Implementa la lógica para cargar la base de conocimientos desde el archivo CSV
    # Puedes personalizar esta función según tus necesidades
    return pd.DataFrame({"pregunta": ["¿Cuál es tu nombre?", "¿Cuál es la capital de Francia?"],
                         "respuesta": ["Soy un asistente AI.", "La capital de Francia es París."]})

def buscar_respuesta(tokens_pregunta):
    conocimientos = cargar_conocimientos()
    # Implementa la lógica para buscar respuestas en la base de conocimientos
    # Puedes personalizar esta función según tus nepip cesidades
    pregunta_str = ' '.join(tokens_pregunta)
    respuesta = conocimientos[conocimientos['pregunta'] == pregunta_str]['respuesta'].values
    return respuesta[0] if len(respuesta) > 0 else "Lo siento, no tengo información sobre eso."

def es_concepto_de_programacion(palabra):
    palabras_clave_programacion = ["programación", "lenguajes", "algoritmos", "desarrollo"]
    return any(keyword in palabra.lower() for keyword in palabras_clave_programacion)

base_conocimientos = {
    ("hola",): "¡Hola! Soy tu asistente AI.",
    ("aprender",): "Soy un ejemplo básico y no tengo la capacidad de aprender de forma continua.",
    ("informacion",): "No tengo información almacenada actualmente.",
    ("programación", "lenguaje", "C#"): "C# es un lenguaje de programación desarrollado por Microsoft...",
    # Agrega más entradas según sea necesario
}

def buscar_respuesta(palabras_clave):
    # Convertir las palabras clave a una tupla para buscar en la base de conocimientos simulada
    clave_busqueda = tuple(palabras_clave)

    # Búsqueda en la base de conocimientos
    respuesta = base_conocimientos.get(clave_busqueda, "Lo siento, no tengo una respuesta para eso en este momento.")

    return respuesta