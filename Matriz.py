def llenar_matriz(matriz,n):
    for i in range(n):
        matriz[i][0] = 1
        matriz[i][n-1] = 1
        matriz[i][i] = 1
        
    return matriz

def mostrar_matriz(matriz,n):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()
            

n = int(input("Ingrese el tamaño de la matris: "))
matriz = [[0] * n for _ in range(n)]
mostrar_matriz(llenar_matriz(matriz,n),n)

       
            
    