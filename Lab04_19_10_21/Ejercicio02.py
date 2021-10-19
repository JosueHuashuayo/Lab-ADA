def every_other(array):
    for i in range(len(array)):
        if i % 2 == 0:
            for j in array:
                print(array[i] + j)
every_other([1,2,3,4])
