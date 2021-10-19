#Convertir from O(n^2) to O(n)
def greatestNumber(array):
    for i in array:
        isValTheGreatest = True
        for j in array:
            if j > 1:
                isValTheGreatest = False
        if isValTheGreatest:
            return i
array=[1,2,3,4,5]
print(greatestNumber(array))
