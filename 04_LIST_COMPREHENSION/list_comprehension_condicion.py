"""lista = [exprecion(elemento) for elemento in objeto_iterable if condicion]"""
"""lista = [exprecion(condicion) for elemento in objeto_iterable]"""


def calcular_cuadrado(numero):
    return numero ** 2

def es_par(numero):
    return numero % 2 == 0

list_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = [calcular_cuadrado(num) for num in list_num ]
print("Lista cuadrados", lista_cuadrados)

lista_cuadrados_pares = [calcular_cuadrado(num) for num in list_num if es_par(num)]
print("Lista cuadrados pares", lista_cuadrados_pares)

lista_resultados = [calcular_cuadrado(num)  if es_par(num) else 0 for num in list_num]
print("Lista resultados", lista_resultados)
