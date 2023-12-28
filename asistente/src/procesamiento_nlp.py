import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("punkt")
nltk.download("stopwords")

def procesar_pregunta(pregunta):
    # Tokenización
    palabras = word_tokenize(pregunta)

    # Eliminación de stopwords
    stop_words = set(stopwords.words("english"))
    palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    palabras_stem = [stemmer.stem(palabra) for palabra in palabras_filtradas]

    return palabras_stem
