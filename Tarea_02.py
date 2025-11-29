class Persona:
    def _init_(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def burbuja(self, vector):
        n = len(vector)
        
        for i in range (n-1):
            for j in range(n-i-1):
                if vector[j] > vector[j+1]:
                    vector[j], vector[j+1] = vector[j+1], vector[j]
        return vector

    def dormir(self):
        print ("La persona duerme")

    def corre(self):
        n = 100
        return n
    
per = Persona("Dayana","35","UPEA")
per.dormir()
per.corre()
vector = [6, 3, 4, 1, 10, 2]
print ("Vector Main: ", vector)
print ("Vector ordenado: ", per.burbuja(vector))