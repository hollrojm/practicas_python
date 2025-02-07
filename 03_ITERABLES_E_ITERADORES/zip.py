nombres = ["Annie", "Lucia", "Hollman", "Ernesto"]
apellidos = ["Rojas","Benavides", "Medina"]

nombre_completo = list(zip(nombres, apellidos))
print(nombre_completo)

nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)

for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)
