def seleccion(vector):
    n = len(vector)
    for i in range(n - 1):
        indice = i
        for j in range(i + 1, n):
            if vector[j] > vector[indice]:
                indice = j
        vector[i], vector[indice] = vector[indice], vector[i]
        
    return vector

vector = [10,5,2,1,11,20,4,2]
print("algortimo selecion sort")
print("Vector original: ", vector)
print("Vector ordenado: ",seleccion(vector))          