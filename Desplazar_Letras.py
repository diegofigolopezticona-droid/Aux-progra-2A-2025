def deplazar(palabra, n):
    nueva = ""
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    for letra in palabra:
        for i in range(len(abc)):
            if letra == abc[i]:
                nueva += abc[(i + n) % 26]
                
        
    return nueva

palabra = input("ingrese palabra: ")
n = int(input("ingrese n: "))

print("nueva palabra : ",deplazar(palabra,n))
        