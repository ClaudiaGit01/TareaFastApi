from fastapi import FastAPI, Query
from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from typing import Optional
import nltk

app = FastAPI() #Crea una instancia de la clase FastAPI 
app.title = "Mi aplicación de películas favoritas con FastAPI"
app.version = "0.0.1"

movies_list = [
    {
        "id": 1,
        "title": "Deadpool y Wolverne",
        "overview": "Deadpool y Wolverine se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 8.5
    },
        {
        "id": 2,
        "title": "Los vengadores",
        "overview": "Los vengadores se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 9.0
    },
        {
        "id": 3,
        "title": "Matrix",
        "overview": "The Matrix se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 9.5
    },
        {
        "id": 4,
        "title": "Rapidos y furiosos",
        "overview": "Rapidos y Furiosos se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 9.5       
        },
        {
        "id": 5,
        "title": "Los Intogables",
        "overview": "Los Intogables se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 9.5       
        },
        {
        "id": 6,
        "title": "Top Gun",
        "overview": "Top Gun se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 9.5       
        },
        {
        "id": 7,
        "title": "Titanic",
        "overview": "Titanic se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 9.5       
        },
        {
        "id": 8,
        "title": "El Padrino",
        "overview": "El Padrino se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 9.5       
        },
        {
        "id": 9,
        "title": "Avatar",
        "overview": "Avatar se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 9.5       
        },
        {
        "id": 10,
        "title": "Batman",
        "overview": "batman se unen en una aventura peligrosa",
        "year": 2024,
        "rating": 9.5
        }       
]
@app.get('/', tags=["Home"])#Definimos una ruta
def message(): # Definimos una función de la ruta
    return HTMLResponse ('<h1>Hello world</h1>') # Devolvemos un string en la respuesta de la ruta

@app.get('/movies/{id}', tags=["Movies"])#Definimos una ruta de la clase FastAPI
def get_movie(id: int):
    for item in movies_list:
        if item['id'] == id:
            return item
    return []

#Tokenizar
@app.post("/tokenize") # Decorador para indicar que es una ruta de la API
def tokenize(text:str): # Funcion que retorna un mensaje
    return preprocessar(text)

def preprocessar(text):
    import json  # Importamos la librería json para trabajar con archivos json
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('punkt')
    tokens = word_tokenize(text)
    result = {word: True for word in tokens}
    print(result)
    return JSONResponse(content={"message":result})

