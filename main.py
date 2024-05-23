from grafica import graficar
from manejo_archivos import get_numbers_from_file
from algoritmos import ord_selection, ord_quick
from tiempos import tiempos_seleccion, tiempos_quicksort

# Archivos
mejor_caso = "mejor_caso.txt"
caso_promedio = "caso_promedio.txt"
peor_caso = "peor_caso.txt"

def mostrar_diccionario(tiempos):
  print(tiempos["mejor_caso"])
  print(tiempos["caso_promedio"])
  print(tiempos["peor_caso"])

def run_caso(archivo, n, opcion):
  arr_selection = get_numbers_from_file(archivo, n)
  arr_quick = get_numbers_from_file(archivo, n)
    
  ord_selection(arr_selection, opcion, tiempos_seleccion)
  ord_quick(arr_quick, opcion, tiempos_quicksort)

def main():

  variables = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

  for i in variables:
    print("Procesando ", i, " entradas...")

    run_caso(mejor_caso, i, "mejor_caso")
    run_caso(caso_promedio, i, "caso_promedio")
    run_caso(peor_caso, i, "peor_caso")

    print("¡Entradas procesadas correctamente!\n")

  # Mejor caso
  y = tiempos_seleccion["mejor_caso"]
  y_2 = tiempos_quicksort["mejor_caso"]

  # Caso promedio
  w = tiempos_seleccion["caso_promedio"]
  w_2 = tiempos_quicksort["caso_promedio"]

  # Peor caso
  z = tiempos_seleccion["peor_caso"]
  z_2 = tiempos_quicksort["peor_caso"]

  graficar(variables, y, y_2, w, w_2, z, z_2)

  # mostrar_diccionario(tiempos_seleccion)
  # mostrar_diccionario(tiempos_quicksort)

main()