"""
Cuando trabajamos en archivos en Python debemos definir su ubicación o ruta.
Para definir la ubicación del archivopodemos usar rutas relativas o rutas 
absolutas.Las relativas se llaman asíporque son relativas a la ubicación del archivo.

"""
import csv
import os
#ruta relativa
ruta = "csv_vacio.csv"
#ruta absoluta
ruta_absoluta = "E:\\practicas\\cursoInLearnig\\05_ARCHIVOS_CSV\\csv_vacio.csv"
ruta_absoluta_os =os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)
#archivo_abierto = open(ruta, "w")
#writer = csv.writer(archivo_abierto, delimiter=",")
#archivo_abierto.close()
