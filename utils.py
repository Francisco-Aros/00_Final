import streamlit as st
import pandas as pd
import os
import requests
import json
from dotenv import load_dotenv
from urllib.parse import quote

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


@st.cache
def carga_data():
  return pd.read_excel("Incendios-Forestales-Los-Lagos-2017-2022.xlsx", header=0)
  #se lee la info de manera óptima

incendios =  carga_data()
incendios["Fecha_de_Proceso"]="08-11-2022"
incendios["Clima"]=""

print(incendios)

  #Obtener parte de la info, se crea un nuevo DataFrame
geo_puntos_comuna = incendios[ ["Temporada", "Región", "Provincia", "Comuna","Inicio", "Detección", "Extinción", "Latitud", "Longitud", "Fecha_de_Proceso", "Clima"]].rename(columns={
    "Inicio": "Fecha_de_inicio",
    "Detección": "Fecha_de_detección",
    "Extinción": "Fecha_de_extinción",
})

print(geo_puntos_comuna)
    


geo_puntos_comuna.to_csv("datosincendios.csv", encoding="utf-8")
geo_puntos_comuna.to_excel("datosincendios.xlsx")
