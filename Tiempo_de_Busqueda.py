import random 
import time

vector = [0] * 50000 # 1 
for i in range(50000):
    vector[i] = random.randint(0,100)

tiempo_inicio = time.time()
vector.sort()
tiempo_final = time.time()

res = tiempo_final - tiempo_inicio

print("tiempo q tardo: ",res) 
