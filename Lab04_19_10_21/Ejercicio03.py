#Ejercicio 03
def twosum(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i!=j and array[i] + array[j] == 10:
                return True
    return False
print(twosum([1,2,3,4,5,6]))
