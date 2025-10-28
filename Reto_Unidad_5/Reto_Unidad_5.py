# RETO UNIDAD 5: ARCHIVOS Y VISUALIZACIÓN.
# Aplicación CLI (Command Line Interface) de análisis y graficación de datos.

import csv
import os
import matplotlib as plt

# Creación de funcion CASE 1 MENÚ PRINCIPAL:

# Se hizo uso del módulo "OS" sugerido por el docente, principalmente para retornar el directorio actual si el usuario no escribe nada al momento de preguntarle y para listar todos los archivos de un directorio.

def LA():
    ruta = input("Ingrese la ruta de la carpeta (o presione Enter para usar la ruta actual): ")
    
    if ruta == "":
        ruta = os.getcwd()     # Si el usuario no escribe nada, se usa la ruta actual.
    
    if not os.path.exists(ruta):     # os.path.exists() verifica si el directorio existe.
        print("La ruta ingresada no existe.")
        return
    
    print(f"Archivos en: {ruta}")
    
    archivos = os.listdir(ruta) # os.listdir() permite listar todos los archivos en el directorio seleccionado.
    if not archivos:
        print("La carpeta está vacía.")
    else:
        for i, archivo in enumerate(archivos, start=1): # Recorre todos los archivos en la lista y comienza en uno para una correcta numeración.
            print(f"{i}. {archivo}")


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
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión, por ejemplo: texto.txt): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    with open(nombre_archivo, "r", encoding="utf-8") as archivo: # Abrimos el archivo como solo lectura y usamos la codificación adecuada para evitar problemas con tiles y letras ñ.
        contenido = archivo.read().lower() # Leemos el archivo. El método lower() para pasar todas las letras a minúscula y trabajar más cómodamente.
    vocales = ["a","e","i","o","u"] # Se crea una lista vacía donde se almacenarán las vocales. Agregamos las vocales iniciales para garantizar el orden en el histograma. Suma una letra de más a cada vocal, pero es irrelevante en la gráfica.
    for i in contenido: # Se usa un bucle para recorrer todas las letras del texto.
        if i in "aeiou": 
            vocales.append(i) # Si la letra pertenece a las vocales, se agrega a la lista.
    plt.hist(vocales, bins=15, edgecolor='black') # Se configura el histograma con ancho de columna del gráfico, color de relleno y color de borde.
    plt.title("HISTOGRAMA DE OCURRENCIAS VOCALES.") # Se asigna un nombre a la gráfica.
    plt.xlabel("Vocales") # Se asignan las vocales a lo largo del eje X.
    plt.ylabel("Frecuencia") # Se asignan las ocurrencias a lo largo del eje Y.
    plt.show() # Se muestra el histograma.

# Creación de funciones CASE 3 MENÚ PRINCIPAL:

def M15PF ():
    nombre_archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: datos.csv): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    archivo = open(nombre_archivo, "r", encoding="utf-8") # Se abre el archivo de texto. Se usa encoding="utf-8" para asegurar que la información se interprete en el formato correcto.
    print("=== PRIMERAS QUINCE (15) FILAS DEL ARCHIVO ===")
    contador = 0 # Usamos un contador para garantizar que solo se mostrarán las primeras 15 líneas.
    for linea in archivo:
        print(linea)
        contador += 1 # Sumamos una unidad al contador, pues ya se ha mostrado una línea.
        if contador == 15: 
            break  # Detiene el ciclo después de 15 líneas.
    archivo.close() # Se cierra el archivo para evitar conflictos al momento de querer modificarlo después.
    print(f"Se mostraron las primeras {contador} líneas del archivo.")


def CE(datos): # La función recibe como argumento la variable datos que contiene la información por colunmas.
    columna = int(input("Ingrese el número de la columna que desea analizar (empezando desde 0): ")) # Permite elegir al usuario la colunma a analizar.
    valores = [] # Se crea una lista vacía para almacenar los datos de la columna específica.
    for fila in datos: # Se usa un bucle for para recorrer cada fila, pues finalmente la colunma requiere filas para almacenar los datos.
        valores.append(fila[columna]) # Se agregan los datos a la lista a medida que se recorren las filas. Se usa [colunma] para asegurar que solo se incluye el dato posicionado en la colunma seleccioanda.
    
    n = len(valores) # Se define una variable para contar cuantos valores tiene la lista, es decir, con cuantos datos se van a calcular las estadísticas.
    
    # Se calcula el promedio.
    suma = 0
    for v in valores:
        suma += v
    promedio = suma / n
    
    # Se calcula la mediana.
    valores_ordenados = sorted(valores) # sorted() permite organizar los datos de menor a mayor, paso estrictamente necesario para calcular la mediana.
    if n % 2 == 0:
        mediana = (valores_ordenados[n//2 - 1] + valores_ordenados[n//2]) / 2 # Si el número de valores es par, indica que la mediana va a estar dada por el promedio de dos valores. Si es impar, va a ser un único elemento.
    else:
        mediana = valores_ordenados[n//2]
    
    # Se calcula la desviación estándar.
    suma_diferencias = 0
    for v in valores:
        suma_diferencias += (v - promedio) ** 2
    desviacion = (suma_diferencias / n) ** 0.5
    
    maximo = max(valores)
    minimo = min(valores)
    
    # Se retornan los resultados en forma de diccionario, para poder mostrarlos después.
    return {
        "Número de datos": n,
        "Promedio": promedio,
        "Mediana": mediana,
        "Desviación estándar": desviacion,
        "Máximo": maximo,
        "Mínimo": minimo
    }
    print (f"===CALCULOS ESTADÍSTICOS===\n Número de Datos ---> {n}\n Promedio ---> {promedio}\n Mediana ---> {mediana}\n Desviación Estándar ---> {desviacion}\n Máximo ---> {maximo}\n Mínimo ---> {minimo}")


def GUCCLD():
  print ("Aún se está trabajando en la función.")


# MENÚ PRINCIPAL.

while True:
    print ("¡Bienvenido! Esta herramienta le permite realizar las siguientes opciones:")
    print (" (1). Listar archivos de la ruta actual o seleccionar una ruta diferente.\n (2). Procesar archivo de texto (.txt).\n (3). Procesar archivo separado por comas (.csv).\n (4). Salir.")
    OPCION = int(input("Seleccione la opción de su preferencia: "))

    match (OPCION):
        case 1:
            LA()
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

