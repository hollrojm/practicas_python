import csv

""" with open ('datos.csv', "r", encoding="utf-8") as archivo:
    reader = csv.reader(archivo, delimiter=",")
    columnas =next(reader)
    print(columnas)
    for linea in reader:
        print(linea[0]) """
        
with open ('datos.csv', "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    
    for linea in reader:
        print(linea['nombre'])