# RETO UNIDAD 5: ARCHIVOS Y VISUALIZACIÓN.
# Aplicación CLI (Command Line Interface) de análisis y graficación de datos.

import csv

# Creación de funciones CASE 2 MENÚ PRINCIPAL:

def CNPYC():
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión, por ejemplo: texto.txt): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    archivo = open(nombre_archivo, "r", encoding="utf-8") # Se abre el archivo de texto. Se usa encoding="utf-8" para asegurar que la información se interprete en el formato correcto.
    contenido = archivo.read() # Leemos los datos del archivo.
    num_palabras = len(contenido.split()) # Se cuenta el número de palabras. El método split permite separar una cadena de texto en elementos diferentes, en este caso, palabras.
    num_caracteres_total = len(contenido) # Se lee el número de caracteres. En ese caso no se usa split, porque no queremos que cada palabra sea un caracter. Se necesita contar cada letra, espacio, signo, etc.
    num_caracteres_sin_espacios = len(contenido.replace(" ", "").replace("\n", "")) # Se lee la cantidad de caracteres, sin incluir los espacios. Reemplazamos lo espacios y los enter para que ahora ya no existan al momento de contar.
    print("=== RESULTADOS ===")
    print(f"Archivo: {nombre_archivo}")
    print(f"Número de palabras: {num_palabras}")
    print(f"Caracteres totales (incluyendo espacios): {num_caracteres_total}")
    print(f"Caracteres sin espacios: {num_caracteres_sin_espacios}")
    archivo.close() # Se cierra el archivo para evitar conflictos al momento de querer modificarlo después.

def RUPPO():
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión, por ejemplo: texto.txt): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    archivo = open(nombre_archivo, "r", encoding="utf-8") # Se abre el archivo de texto. Se usa encoding="utf-8" para asegurar que la información se interprete en el formato correcto.
    contenido = archivo.read() # Leemos los datos del archivo.
    palabra_buscar = input("Ingrese la palabra que desea reemplazar: ") # Se lee la palabra a reemplazar.
    palabra_reemplazo = input("Ingrese la nueva palabra: ") # Se lee la nueva palabra.
    ocurrencias = contenido.count(palabra_buscar) # Permite contar cuántas veces aparece la palabra antes de reemplazar.
    if ocurrencias == 0:
        print(f"La palabra '{palabra_buscar}' no se encontró en el archivo.") # No se puede reemplazar una palabra que no está en el archivo.
    else:
        nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazo) # Se reemplaza la palabra.
        with open(nombre_archivo, "w", encoding="utf-8") as archivo: # Permite abrir el archivo, pero esta vez con la posibilidad de escribir en él. 
            archivo.write(nuevo_contenido) # Escribe las nuevas palabras en el archivo.
        print("=== REEMPLAZO COMPLETADO CON ÉXITO ===")
        print(f"Archivo: {nombre_archivo}")
        print(f"Palabra reemplazada: '{palabra_buscar}' ---> '{palabra_reemplazo}'")
        print(f"Ocurrencias reemplazadas: {ocurrencias}")
        # No se usa close() porque el archivo se cierra automáticamente al salir del bloque with.

def HDODLV():
 print ("Aún se está trabajando en la función.")

# Creación de funciones CASE 3 MENÚ PRINCIPAL:

def M15PF ():
    nombre_archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: datos.csv): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    archivo = open(nombre_archivo, "r", encoding="utf-8") # Se abre el archivo de texto. Se usa encoding="utf-8" para asegurar que la información se interprete en el formato correcto.
    print("=== PRIMERAS QUINCE (15) FILAS DEL ARCHIVO ===")
    contador = 0 # Usamos un contador para garantizar que solo se mostrarán las primeras 15 líneas.
    for linea in archivo:
        print(linea.strip())  # El módulo strip permite eliminar los saltos de línea y espacios en blanco al inicio y al final de la cadena.
        contador += 1 # Sumamos una unidad al contador, pues ya se ha mostrado una línea.
        if contador == 15: 
            break  # Detiene el ciclo después de 15 líneas.
    archivo.close() # Se cierra el archivo para evitar conflictos al momento de querer modificarlo después.
    print(f"Se mostraron las primeras {contador} líneas del archivo.")


def CE():
  print ("Aún se está trabajando en la función.")

def GUCCLD():
  print ("Aún se está trabajando en la función.")


# MENÚ PRINCIPAL.

while True:
    print ("¡Bienvenido! Esta herramienta le permite realizar las siguientes opciones:")
    print (" (1). Listar archivos de la ruta actual o seleccionar una ruta diferente.\n (2). Procesar archivo de texto (.txt).\n (3). Procesar archivo separado por comas (.csv).\n (4). Salir.")
    OPCION = int(input("Seleccione la opción de su preferencia: "))

    match (OPCION):
        case 1:
            print ("Aún se está trabajando en la función.")
        case 2:
            OPCION2 = int(input("Ha seleccionado la opción que le permite procesar archivo de texto (.txt)\n Esta opción le permite: \n (1). Contar número de palabras y caracteres.\n (2). Reemplazar una palabra por otra.\n (3). Histograma de ocurrencia de las vocales.\n (4). Salir.\n Ahora, seleccione qué desea realizar con su archivo: "))
            match (OPCION2):
                case 1:
                    CNPYC()
                case 2:
                    RUPPO()
                case 3:
                    HDODLV()
                case 4:
                    print ("¡Hasta luego!\n Saliendo del programa...")
                    break
                case _:
                    print ("Por favor, seleccione una opción válida.")
        case 3:
            OPCION3 = int(input("Ha seleccionado la opción que le permite procesar archivos (.csv).\n Ahora, seleccione qué desea realizar con su archivo:\n (1). Mostrar las 15 primeras filas.\n (2). Calcular estadísticas.\n (3). Graficar una columna completa con los datos.\n (4). Salir."))
            match (OPCION3):
                case 1:
                    M15PF()
                case 2:
                    CE()
                case 3:
                    GUCCLD()
                case 4:
                    print ("¡Hasta luego!\n Saliendo del programa...")
                    break
                case _:
                    print ("Por favor, seleccione una opción válida.")
        case 4:
            print ("¡Hasta luego!\n Saliendo del programa...")
            break
        case _:
            print ("Por favor, seleccione una opción válida.")

