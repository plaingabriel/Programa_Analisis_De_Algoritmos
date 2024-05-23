def guardarTiempo(ti, tf, opcion, tiempos):
  tiempo_total = tf - ti
  tiempo_total *= 1000

  tiempos[opcion].append(tiempo_total)
