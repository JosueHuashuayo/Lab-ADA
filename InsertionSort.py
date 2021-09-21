def insertionSort(array):
    for i in range(1,len(array)):
        aux = array[i]
        j = i-1
        while j >= 0 and array[j] > aux :
                array[j+1] =array[j]
                j = j - 1
        array[j+1]=aux
    print(array)


arr=[7,5,4,9,6,2,1,3,8]
insertionSort(arr)