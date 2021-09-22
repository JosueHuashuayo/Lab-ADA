import time
import random
from typing import final
def Busqueda(array, numero):
    for n in range(len(array)):
        if array[n] == numero:
            print("lo encontro")

def insertionSort(array):
    for i in range(1,len(array)):
        aux = array[i]
        j = i-1
        while j >= 0 and array[j] > aux :
                array[j + 1] = array[j]
                j = j - 1
        array[j + 1] = aux
    print(array)

def n_values(n):
    array=[ ]
    for i in range(n):
        array.append(random.randint(1,n))
    return array

inicio = time.time()
array = n_values(10000)      
# Busqueda(array,numero)
insertionSort(array)
final = time.time()

print(final-inicio)



