import funcionesEstadisticaMundial as fem

""" RETO SEMANA 7
  Santiago Correa Restrepo
  cc 75105613
  Estadistica Mundial 
  Grupo 96
  Fecha 22 junio 2021

Referencia de datos obtenidos de https://www.worldometers.info/world-population/#region
"""""
#---------------- Zona librerias------------
"""
TODO
Importar las librerias necesarias
"""
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

def menuOpciones():
  bandera=0
  while(bandera == 0):
    print("\n ||||---------------POBLACIÓN MUNDIAL POR REGION---------------|||| ")
    print("   1. Mostrar regiones y datos de poblacion (1) ")
    print("   ...............................")
    print("   2. Mostrar estadísticas de las regiones (2) ")
    print("   ...............................")
    print("   3. Mostrar regiones ordenadas por poblacion - edad - tasa de fertilidad (3) ")
    print("   ...............................")
    print("   4. Mostrar información de una region (4) ")
    print("   ...............................")
    print("   5. Graficar tasa de fertilidad por regiones (5) ")
    print("   ...............................")
    print("   6. Graficar porcentaje de poblacion por regiones (6) ")
    print("   ...............................")
    print("\n .............OPCIONALES..................")
    print("....")
   
    opcion = int(input("\n Seleccione una opción: "))

    if opcion == 1:
      fem.mostrar_datos_regiones()
    
    if opcion == 2:
      fem.mostrar_estadisticas_regiones()
    
    if opcion == 3:
      selection = int(input('Escoja columna a ordenar sus datos: \n 1. poblacion \n 2. Edad media \n 3. Tasa de fertilidad: \n'))

      fem.ordenar_regiones(selection)

    if opcion == 4:
      nombre_region = input('Ingrese nombre de la región: ')
      fem.mostrar_informacion_region(nombre_region)
    
    if opcion == 5:
      fem.graficar_fertilidad_regiones()

    if opcion == 6:
      fem.graficar_regiones_porcentaje()
    
    if opcion == 7:
      fem.averageAges()
    
    elif(opcion==0):
      bandera=1

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#Recuerde comentar la siguiente instrucción para ejecutar los test
menuOpciones()



