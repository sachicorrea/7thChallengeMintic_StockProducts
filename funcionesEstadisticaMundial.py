import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#---------------- Zona librerias------------
"""
TODO
Importar las librerias necesarias
"""

#---------------- Zona de dataframes------------
poblacion={"region":["Asia","Africa","Europa", "Latino America", "Norte America", "Oceania"], 
"poblacion":[4641054775,134059814, 747636026, 653962331, 368869647, 42677813],
"densidad":[150, 45, 34, 32, 20, 5],
"t. fertilidad":[2.2, 4.4, 1.6, 2, 1.8, 2.40],
"edad media":[32,20,43,31,39,33],
"porcentaje":[59.5, 17.2, 9.6, 8.4, 4.7, 0.5]}

df = pd.DataFrame(data=poblacion)

#---------------- Zona librerias------------

def mostrar_datos_regiones():
  """
  TODO 
  Mostrar los datos de las regiones. region, poblacion, densidad, fertilidad, edad y porcentaje mundo
  """
  print(df)

def mostrar_estadisticas_regiones():
  """
  TODO 
  Mostrar estadisticas de las regiones como: cantidad de datos, media, valor minimo, valor maximo, etc
  """
  print(df.describe())

def ordenar_regiones(selection):
  """
  TODO 
  Solicita al usuario si quiere ordenar las regiones por poblacion o edad o tasa de fertilidad. Muestra la tabla ordenada 
  Si el usuario ingresa una opción no valida se muestre el mensaje:
  ERROR: dato no valido
  """
  if selection == 1:
    ordered = df.sort_values(by='poblacion')
  
  elif selection == 2:
    ordered = df.sort_values(by='edad media')
  
  elif selection == 3:
    ordered = df.sort_values(by='t. fertilidad')
  
  else:
    ordered = "ERROR: dato no valido"
  
  print(ordered)

def mostrar_informacion_region(nombre_region):
  """
  TODO 
  Muestra los datos de la region del parametro. Se debe considerar que si el usuario ingresa mayusculas o minisculas es indiferente si el contenido corresponde.
  Si la region no existe en la tabla se muestra el mensaje:
  ERROR: region no valida
  """
  region_modifyied = nombre_region.lower().title()
  
  locations = list(df["region"])
  
  if region_modifyied in locations:
    print(df.loc[(df['region'] == region_modifyied)])
  else:
    print("ERROR: region no valida")

def graficar_fertilidad_regiones():
  """
  TODO 
  Muestra en un histograma los datos de la region y tasa de fertilidad
  """
  location = list(df["region"])
  fertility = list(df["t. fertilidad"])

  x = np.array(location)
  y = np.array(fertility)

  plt.xlabel("region")
  plt.ylabel("tasa natalidad")
  plt.bar(x,y)
  plt.show()

def graficar_regiones_porcentaje():
  """
  TODO 
  Muestra en un grafico tipo pie los datos de la region y el porcentaje de población que ocupa en el mundo
  """
  percPopulation = list(df["porcentaje"])
  labelsRegions = list(df["region"])

  y = np.array(percPopulation)
  mylabels = np.array(labelsRegions)

  plt.pie(y, labels = mylabels)
  plt.show()

def averageAges():
  listAges = list(df["edad media"])
 
  if len(listAges) == 0:
    print("No existen edades medias ingresadas")
  else:
    averageAgesRegions = sum(listAges) / len(listAges)
    print("El promedio de edad media de las regiones es: ", averageAgesRegions)