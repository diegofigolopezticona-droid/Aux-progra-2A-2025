import os

buscar = "Perfil de tesis corregido(1).pdf"

if os.path.exists(buscar):
    with open (buscar, "r") as archivo:
        print(archivo.read())
else:
    print("Archivo no existe")