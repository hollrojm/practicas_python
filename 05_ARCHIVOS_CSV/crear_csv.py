"""
CSV es el acrónimo de Comma Separated Valuesque en español significa 
Valores separados por comas.

"""
import csv

ruta = "csv_vacio.csv"

archivo_abierto = open(ruta, "w")
writer = csv.writer(archivo_abierto, delimiter=",")
archivo_abierto.close()
