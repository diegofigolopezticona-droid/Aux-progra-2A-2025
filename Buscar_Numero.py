def busqueda_lineal(x,vector):
    posicion = [0] * Tamaño_vector(vector)
    contador = 0
    for i in range(Tamaño_vector(vector)):
        if vector[i] == x:
            posicion[contador] = i
            contador += 1
    return posicion
    
def llenar_vector(n):
    vector = [0] * n
    for i in range(n):
        vector[i] = int(input("Ingrese numero"))
    return vector
    
def Tamaño_vector(vector):
    contador = 0
    for _ in vector:
        contador += 1
    return contador
    

n = int(input("ingrese el tamaño del vector: "))
x = int(input("Ingrese el numero a Buscar: "))
vector = llenar_vector(n)
print("el numero a buscar es :", x )
print("Busqueda lineal", ", se encuentras en las posiciones ",busqueda_lineal(x,vector))

