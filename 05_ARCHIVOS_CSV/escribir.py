import csv

columnas = ["nombre", "apellido", "edad"]
dato = ["Juan", "Perez", 30]


datos_lista = [
    ["Juan", "Perez", 30],
    ["Maria", "Gomez", 25],
    ["Carlos", "Lopez", 35]
]

datos_dict = [
    {"nombre": "Hollman", "apellido": "Perez", "edad": 41},
    {"nombre": "Annie", "apellido": "Gomez", "edad": 6},
    {"nombre": "LUcia", "apellido": "Lopez", "edad": 28}
]

#archivo = open("datos.csv", "w")
#writer = csv.writer(archivo, delimiter=",")
#archivo.close()

""" with open("datos.csv", "w", newline= "") as archivo:
    writer = csv.writer(archivo, delimiter=",")
    writer.writerow(columnas)
    solo un set de datos
    #writer.writerow(dato)
    debemos invocar, en vez de la función writerow, la función writerows 
    writer.writerows(datos_lista) """
   

"""datos que tengamos almacenados en listas de diccionarios"""
with open("datos.csv", "w", newline= "") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=columnas)
    writer.writeheader()
    writer.writerows(datos_dict)
