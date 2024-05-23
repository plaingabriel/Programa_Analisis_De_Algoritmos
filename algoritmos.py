import sys
import time

sys.setrecursionlimit(10**6)

from guardar_tiempo import guardarTiempo

def ord_selection(arreglo, opcion, tiempos):

  tiempo_inicial = time.time()

  for i in range(len(arreglo) - 1):        # <-- bucle padre
    menor = i # primer elemento por default será el mínimo

    for j in range(i + 1, len(arreglo)): # <-- bucle hijo
      if arreglo[j] < arreglo[menor]:
        menor = j

    if menor != i:
      arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]

  tiempo_final = time.time()
  guardarTiempo(tiempo_inicial, tiempo_final, opcion, tiempos)

def quicksort(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def ord_quick(arr, opcion, tiempos):

  tiempo_inicial = time.time()

  quicksort(arr)

  tiempo_final = time.time()
  guardarTiempo(tiempo_inicial, tiempo_final, opcion, tiempos)
  