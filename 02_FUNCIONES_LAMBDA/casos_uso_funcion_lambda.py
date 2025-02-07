lista_numero = [1,2,3,4,6,7,8]

lista_pares = list(filter(lambda numero: numero%2 == 0, lista_numero))
print(lista_pares)

nueva_lista = list(map(lambda numero: numero*10, lista_numero))
print(nueva_lista)