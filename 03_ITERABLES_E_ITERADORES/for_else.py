lista_nombres = ["Annie", "Hollman", "Lucia", "Sandra"]

for nombre in lista_nombres:
    print(nombre)
else:
    print("Ciclo terminado")

for nombre in lista_nombres:
    print(nombre)
    if nombre == "Lucia":
        break
else:
    print("Ciclo terminado")