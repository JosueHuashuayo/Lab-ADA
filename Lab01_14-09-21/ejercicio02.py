#Ejercicio 02
def arrayInvertido(array):
    #Truco de sintaxis
    #Consiste en hacer un tipo de arraycopy empezando de adelante hacia atras
    arrayInv = array[::-1]
    return arrayInv


array = [1, 2, 3, 4]
print(arrayInvertido(array))
