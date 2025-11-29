# Leonel Capajaña Colquehuanca  2 A

import os

ARCHIVO = "sis211.txt"

def crearArchivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as file:
            pass
        print ("Archivo creado...")
    else:
        print ("El archivo existe...")

def guardarRegistro():
    print ("Ingrese los datos del estudiante: ")
    ru = input ("R.U. : ")
    ci = input ("C.I. : " )
    apellido = input ("Apellido: ")
    nombre = input ("Nombre: ")
    sexo = input ("Sexo: ")
    nota = input ("Nota: ")

    linea = f"{ru}, {ci}, {apellido}, {nombre}, {sexo}, {nota}"

    with open(ARCHIVO, "a") as file:
        file.write(linea)

    print ("Registrado correctamente...")

def cargarDatos():
    estudiante = []
    if not os.path.exists(ARCHIVO):
        return estudiante
    
    with open(ARCHIVO, "r") as file:
        for linea in file:
            partes = linea.strip().split(",")
            if len(partes) == 6:
                estudiante.append(partes)
    return estudiante

def mostrar():
    estudiantes = cargarDatos()
    print("\n LISTA DE ESTUDIANTES ")
    for e in estudiantes:
        print (e)
    print()

def modificar():
    estudiantes = cargarDatos()
    ru = input ("Ingrese RU del estudiante a modificar: ")
    encontrado = False
    for i in range(len(estudiantes)):
        if estudiantes[i][0] == ru:
            print ("Datos actuales del estudiante: ", estudiantes[i])
            estudiantes[i][2] = input("Ingrese nuevo apellido: ")
            estudiantes[i][3] = input("Ingrese nuevo nombre: ")
            estudiantes[i][4] = input("Ingrese nuevo sexo: ")
            estudiantes[i][5] = input("Ingrese nuevo nota: ")  

            encontrado = True
            break

    if encontrado:
        with open(ARCHIVO, "w") as file:
            for e in estudiantes:
                file.write(",".join(e)+ "\n")
            print ("Registtro modificado correctamente")
    
    else:
        print ("RU no encontrado....")

def  main():
    while True:
        print("\n ============= MENU PRINCIPAL =============")
        print ("1. Crear archivo")
        print ("2. Guardar archivo")
        print ("3. Mostrar archivo")
        print ("4. Modificar archivo")
        print ("5. Salir")

        opcion = input ("Ingrese una opción: ")

        if opcion == "1": crearArchivo()
        elif opcion == "2": guardarRegistro()
        elif opcion == "3": mostrar()
        elif opcion =="4": modificar()
        elif opcion == "5":
            print ("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

main()