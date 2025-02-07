def funcion_kwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")
    

funcion_kwargs(nombre="Hollman", apellido = "Rojas")

    