import os

nombre = "Archivo"

try:
    os.remove(nombre)
    print("Archivo eliminado ")
except FileNotFoundError:
    print("Error en el archivo")