import time
import random

n = 50000
vector = [0]*n

for i in range(0, n):
    vector [i] = random.randint(0, 100)

def selection_sort(vector):
    for i in range(len(vector)):
        min_inx = i
        for j in range (i+1, len(vector)):
            if vector[j] < vector[min_inx]:
                min_inx = j
                vector [j], vector[min_inx] = vector[min_inx], vector [j]

    return vector

time1 = time.time()
vector_0 = selection_sort(vector)
time2 = time.time()
print(f"Tiempo de selection Sort : {time2 - time1} segundos")