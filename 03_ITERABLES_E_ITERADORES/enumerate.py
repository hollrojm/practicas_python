nombres = ["Annie", "Hollman", "Lucia", "Sandra"]

nombres_enumerados = enumerate(nombres , start=5)
print(list(nombres_enumerados))

for indice, elemento in enumerate(nombres):
    print(indice, elemento)