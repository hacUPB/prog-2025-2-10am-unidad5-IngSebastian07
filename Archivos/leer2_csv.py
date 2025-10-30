import csv

with open('C:\\Users\\USUARIO\\OneDrive\\Documentos\\Ingeniería Aeronáutica UPB\\S2 - Ingeniería Aeronáutica - UPB\\Programación\\Unidad_5\\ArchivoPruebaExcel.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile,delimiter= ";") # Se utiliza el método reader.
    encabezado = next(lector) # El encabezado pertenece aunalista diferente a la lista de los datos. Con eso, "cortamos" el encabezado y se pasa a la siguiente fila.
    densidad = []              # Se crea una lista vacía.
    print(encabezado[3])
    for fila in lector:          # Con el for se itera sobre el objeto para leer.
        fila[3] = fila[3].replace(',','.') # Se genera un nuevo objeto. Se cambia "," por "."
        dato = float(fila[3])      # Se convierte a entero.
        densidad.append(dato)     # Se agrega el dato a la lista.

print(densidad)
