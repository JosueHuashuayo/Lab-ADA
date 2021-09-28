import time
import random

# Algoritmo de Busqueda lineal
def Busqueda(array, numero):
    for n in range(len(array)):
        if array[n] == numero:
            return True

# Generador de matriz con numeros aleatorios
def n_values(n):  
    array=[ ]
    for i in range(n):
        array.append(random.randint(1,n))
    return array

#Tiempo computacional usando la libreria time
inicio = time.time()
numero = 8
array = n_values(100)
print(array)
if Busqueda(array,numero) == True:
    print("lo encontro")
else:
    print("no se encuentra")
final = time.time()
tiempo_computacional= final - inicio
print(tiempo_computacional)



