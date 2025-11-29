# Archivos - Crear
nombre = input ("Ingrese nombre de archivo: ")
contenido = input("Ingrese el contenido: ")

with open (nombre, "w") as archivo:
    archivo.write(contenido)

print ("Archivo creado")