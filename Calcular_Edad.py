# 19.Realiza una función que calcule la edad de un individuo a partir de la fecha de nacimiento.
def calcular_edad(fecha_nacimiento):
    año_hoy = 2025
    año_nac = int(fecha_nacimiento[6:])
    edad = año_hoy - año_nac
    return edad

fecha = input("ingrese la fecha nacimiento: ")
print("edad = ", calcular_edad(fecha))