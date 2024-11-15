from fastapi import FastAPI 
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse # Importamos la libreria JSONResponse
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
        "rating": 8.5
    },
    {
        "id": 3,
        "title": "Scare face",
        "overview": "Gran clásico de acción",
        "year": 1979,
        "rating": 9.0
    },
    {
        "id": 4,
        "title": "Brave Hearth",
        "overview": "Película de drama y acción",
        "year": 2001,
        "rating": 9.5
    },
    {
        "id": 5,
        "title": "La vida es bella",
        "overview": "Película de drama, guerra y speración",
        "year": 2011,
        "rating": 9.5
    },
    {
        "id": 6,
        "title": "Terminator",
        "overview": "Acción y ciencia ficción",
        "year": 2013,
        "rating": 9.0
    },
    {
        "id": 7,
        "title": "Ninja Scroll",
        "overview": "Pelicul animada sobe los Roning",
        "year": 1995,
        "rating": 9.0
    },
    {
        "id": 8,
        "title": "El Code de Montecristo",
        "overview": "Representación de la gran obra de litertura clásica",
        "year": 2024,
        "rating": 9.0
    },
    {
        "id": 9,
        "title": "7 hombres en pugna",
        "overview": "Gran lásico jurídico",
        "year": 1980,
        "rating": 9.5
    },
    {
        "id": 10,
        "title": "El origen",
        "overview": "Interesante postulado obre los sueños y la realidad",
        "year": 2015,
        "rating": 9.5
    }
]

@app.get('/', tags=["Home"])#Definimos una ruta
def message(): # Definimos una función de la ruta
    return HTMLResponse ('<h1>Hello world</h1>') # Devolvemos un string en la respuesta de la ruta

@app.get('/movies', tags=["Movies"])#Definimos una ruta de la clase FastAPI
def get_movies(): 
    return movies_list

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

# para correr la app: uvicorn main:app --reload
# uvicorn nombreApp:app --reload --port 5000 
# swagger: http://127.0.0.1:5000/docs#/