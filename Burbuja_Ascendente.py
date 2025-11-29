def burbuja(vector):
    n = len(vector)

    for i in range(n - 1):
        for j in range( n - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector

vector = [10,5,2,1,11,20,4,2]
print("Vector original: ", vector)
print("Vector ordenado: ",burbuja(vector))           