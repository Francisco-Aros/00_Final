import requests
import json
import os
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

datos_clima=os.getenv("API_KEY")

lista_comunas = [
  "Ancud",
  "Calbuco",
  "Castro",
  "Chaitén",
  "Chonchi",
  "Cochamó"
]
clima = []

for ubicacion in lista_comunas:
  # Acá se ajusta el nombre de la comuna para hacerla compatible a consulta a la API.
  # Además se agrega una coma y el código de país al que pertenece la comuna, en este caso "CL" por ser Chile.
  ubicacion = quote(ubicacion) + ",CL"

  URL = f"https://api.openweathermap.org/data/2.5/weather?q={ubicacion}&appid={datos_clima}&units=metric&lang=es"
  datos = requests.get(URL)
  datos_json = datos.json()
  temperatura = datos_json
  clima.append(temperatura)

print("Comunas: ",lista_comunas)
print("Clima: ", clima)