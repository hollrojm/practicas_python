def calcular_cuadradro(numero):
    return numero **2


lista_num=[1,2,3,4,5,6,7,8,9,10]
"""lista_cuadrados = []

for num in lista_num:
    cuadrado = calcular_cuadradro(num)
    lista_cuadrados.append(cuadrado)

print(lista_cuadrados)"""

#Usando map
lista_cuadrados = list(map(calcular_cuadradro, lista_num))
print(lista_cuadrados)