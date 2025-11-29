# Archivos - Crear
nombre = "Archivo.txt"

with open (nombre, "r") as archivo:
    print ("Contenido del archivo")
    print (archivo.read())

print ("Archivo creado :)")