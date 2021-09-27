import time
import random
# Algoritmo insertionsort
def insertionSort(array):
    for i in range(1,len(array)):
        aux = array[i]
        j = i-1
        while j >= 0 and array[j] > aux :
                array[j+1] =array[j]
                j = j - 1
        array[j+1]=aux
    print(array)
    
# Generador de matriz con numeros aleatorios
def n_values(n):  
    array=[ ]
    for i in range(n):
        array.append(random.randint(1,n))
    return array

inicio=time.time()
array = n_values(10000)
insertionSort(array)
print(array)
final=time.time()
tiempo_computacional= final-inicio
print(tiempo_computacional)