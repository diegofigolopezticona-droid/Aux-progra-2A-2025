def tamaño():
    n = int ( input ("Ingrese el tamaño del vector: "))
    return n

def vector(n):
    vector = []
    for i in range(n):
        a = int ( input (f"Posicion {i+1}. "))
        vector.append(a)
    return vector

def burbuja(vector):
    n = len(vector)
    for i in range (n-1):
        for j in range(n-i-1):
            if vector[j] < vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector

n = tamaño()
vector = vector(n)
print (vector)
ordenado = burbuja(vector)
print (ordenado)