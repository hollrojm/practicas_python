def clacular_cuadrado(numero):
    return numero ** 2

lista_num = [1,2,3,4,5,6,7,8,9,10]

lista_pares= []

for num in lista_num:
    #cuadrado = clacular_cuadrado(num)
    if (cuadrado := clacular_cuadrado(num)) %2 == 0:
        lista_pares.append(cuadrado)    
       # print(f"Cuadrado de {num} es {cuadrado} y es par")
    #else:
        #print(f"Cuadrado de {num} es {cuadrado} y es impar")

print("Ciclo for", lista_pares)
pares_comprenhension = [cuadrado for num in lista_num if (cuadrado := clacular_cuadrado(num)) %2 == 0]
print("List comprehension walrus", pares_comprenhension)
    