# 18. Realiza una función que reciba una cadena reemplace las vocales por números del 1 al 5.

def reemplza_vocales(cadena):
    nueva_cadena = ""
    for c in cadena:
        if c in "aA":
            nueva_cadena += "1"
        elif c in "eE":
            nueva_cadena += "2"
        elif c in "iI":
            nueva_cadena += "3"
        elif c in "oO":
            nueva_cadena += "4"
        elif c in "uU":
            nueva_cadena += "5"
        else:
            nueva_cadena += c
    return nueva_cadena

texto = input("Ingrese nueca cadena: ")
print("La nueva cadena es: ",reemplza_vocales(texto))
            