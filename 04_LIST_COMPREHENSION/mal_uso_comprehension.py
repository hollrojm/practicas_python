# caso 1
total = sum([num for num in range(100)])
#corrección
total = sum(num for num in range(100))

#caso 2
[print(elemento) for elemento in range(10)]
#corrección
for elemento in range(10):
    print(elemento)


#caso 3
lista_anidada = [[1,2,3],[4,5,6],[7,8,9]]

valores_lista = [numero for elemento in lista_anidada for numero in elemento]
print(valores_lista)

#corrección
lista_anidada = [[1,2,3],[4,5,6],[7,8,9]]
valores_lista = []
for elemento in lista_anidada:
    for numero in elemento:
        valores_lista.append(numero)
print(valores_lista)