import matplotlib.pyplot as plt
import numpy as np

def graficar(eje_x, tiempo1_mejor_caso, tiempo2_mejor_caso, tiempo1_caso_promedio, tiempo2_caso_promedio, tiempo1_peor_caso , tiempo2_peor_caso):

  x = np.array(eje_x)
  y = np.array(tiempo1_mejor_caso)
  y_2 = np.array(tiempo2_mejor_caso)
  w = np.array(tiempo1_caso_promedio)
  w_2 = np.array(tiempo2_caso_promedio)
  z = np.array(tiempo1_peor_caso)
  z_2 = np.array(tiempo2_peor_caso)

# Valores a graficar

  def crear_subplot(pos, x, y, y_2, title):
    plt.subplot(pos)
    plt.plot(x, y, x, y_2)
    plt.xlabel('n')
    plt.ylabel('t(n) (ms)')
    plt.legend(['Selection Sort', 'Quick Sort'])
    plt.title(title)

  crear_subplot(221, x, y, y_2, 'Mejor Caso')
  crear_subplot(222, x, w, w_2, 'Caso Promedio')
  crear_subplot(223, x, z, z_2, 'Peor Caso')

  plt.show()