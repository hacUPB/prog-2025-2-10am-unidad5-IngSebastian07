import csv

with open('C:\\Users\\USUARIO\\OneDrive\\Documentos\\Ingeniería Aeronáutica UPB\\S2 - Ingeniería Aeronáutica - UPB\\Programación\\Unidad_5\\ArchivoPruebaExcel.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile,delimiter= ";") # Se utiliza el método reader.
    encabezado = next(lector) # El encabezado pertenece aunalista diferente a la lista de los datos. Con eso, "cortamos" el encabezado y se pasa a la siguiente fila.
    presion = []
    print(encabezado[0])
    for fila in lector:          # Con el for se itera sobre el objeto para leer.
        dato = int(fila[0])      # Se convierte en entero.
        presion.append(dato)     # Se agrega el dato a la lista.

print(presion)