def get_numbers_from_file(file_name, n):
  numbers = []

  with open(file_name) as file:

    lineas = file.readlines()

    for linea in lineas:
      numbers.append(int(linea))
  
  return numbers[:n+1]