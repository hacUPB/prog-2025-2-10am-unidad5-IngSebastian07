# RETO UNIDAD 5: ARCHIVOS Y VISUALIZACIÓN.
# Aplicación CLI (Command Line Interface) de análisis y graficación de datos.

import csv
import os
import matplotlib.pyplot as plt

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
        for i, archivo in enumerate(archivos, start=1):  # Recorre todos los archivos en la lista y comienza en uno para una correcta numeración.
            # ¡DECLARACIÓN DE IA! Se hizo uso de IA para saber cómo se podía enumerar cada archivo empezando en 1.
            print(f"{i}. {archivo}")


# Creación de funciones CASE 2 MENÚ PRINCIPAL:

def CNPYC():
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión, por ejemplo: texto.txt): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    ruta = "./Reto_Unidad_5/" + nombre_archivo # Se ingresa la ruta del archivo, para leerlo correctamente.
    with open(ruta, "r", encoding="utf-8") as archivo: # Se abre el archivo de texto. Se usa encoding="utf-8" para asegurar que la información se interprete en el formato correcto.
        contenido = archivo.read() # Leemos los datos del archivo.
    num_palabras = len(contenido.split()) # Se cuenta el número de palabras. El método split permite separar una cadena de texto en elementos diferentes, en este caso, palabras.
    num_caracteres_total = len(contenido) # Se lee el número de caracteres. En ese caso no se usa split, porque no queremos que cada palabra sea un caracter. Se necesita contar cada letra, espacio, signo, etc.
    num_caracteres_sin_espacios = len(contenido.replace(" ", "").replace("\n", "")) # Se lee la cantidad de caracteres, sin incluir los espacios. Reemplazamos lo espacios y los enter para que ahora ya no existan al momento de contar.
    print("=== RESULTADOS ===")
    print(f"Archivo: {nombre_archivo}")
    print(f"Número de palabras: {num_palabras}")
    print(f"Caracteres totales (incluyendo espacios): {num_caracteres_total}")
    print(f"Caracteres sin espacios: {num_caracteres_sin_espacios}")

def RUPPO():
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión, por ejemplo: texto.txt): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    ruta = "./Reto_Unidad_5/" + nombre_archivo # Se ingresa la ruta del archivo, para leerlo correctamente.
    with open(ruta, "r", encoding="utf-8") as archivo: # Se abre el archivo de texto. Se usa encoding="utf-8" para asegurar que la información se interprete en el formato correcto.
        contenido = archivo.read() # Leemos los datos del archivo.
    palabra_buscar = input("Ingrese la palabra que desea reemplazar: ") # Se lee la palabra a reemplazar.
    palabra_reemplazo = input("Ingrese la nueva palabra: ") # Se lee la nueva palabra.
    ocurrencias = contenido.count(palabra_buscar) # Permite contar cuántas veces aparece la palabra antes de reemplazar.
    if ocurrencias == 0:
        print(f"La palabra '{palabra_buscar}' no se encontró en el archivo.") # No se puede reemplazar una palabra que no está en el archivo.
    else:
        nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazo) # Se reemplaza la palabra.
        with open(ruta, "w", encoding="utf-8") as archivo: # Permite abrir el archivo, pero esta vez con la posibilidad de escribir en él. 
            archivo.write(nuevo_contenido) # Escribe las nuevas palabras en el archivo.
        print("=== REEMPLAZO COMPLETADO CON ÉXITO ===")
        print(f"Archivo: {nombre_archivo}")
        print(f"Palabra reemplazada: '{palabra_buscar}' ---> '{palabra_reemplazo}'")
        print(f"Ocurrencias reemplazadas: {ocurrencias}")
        # No se usa close() porque el archivo se cierra automáticamente al salir del bloque with.

def HDODLV():
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión, por ejemplo: texto.txt): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    ruta = "./Reto_Unidad_5/" + nombre_archivo # Se ingresa la ruta del archivo, para leerlo correctamente.
    with open(ruta, "r", encoding="utf-8") as archivo: # Se abre el archivo de texto. Se usa encoding="utf-8" para asegurar que la información se interprete en el formato correcto.
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
    # ¡DECLARACIÓN DE IA! Se hizo uso de IA para entender a qué correspondía cada configuración del gráfico.

# Creación de funciones CASE 3 MENÚ PRINCIPAL:

def M15PF ():
    nombre_archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: datos.csv): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    ruta = "./Reto_Unidad_5/" + nombre_archivo # Se ingresa la ruta del archivo, para leerlo correctamente.
    with open(ruta, "r", encoding="latin-1") as archivo: # Se abre el archivo de texto. Se usa encoding="latin-1" para asegurar que la información se interprete en el formato correcto.
        # ¡DECLARACIÓN DE IA! Se hizo uso de IA para corregir un error con la codificación. Sugirió usar "latin-1" y resultó corrigiendo el error.
        print("=== PRIMERAS QUINCE (15) FILAS DEL ARCHIVO ===")
        contador = 0 # Usamos un contador para garantizar que solo se mostrarán las primeras 15 líneas.
        for linea in archivo:
            print(linea.strip().replace(',', ' | ')) # Imprimimos cada línea. El módulo .strip() permite quitar saltos de línea. # Al reemplazar comas por barras, nos permite una visualización más agradable al momento de ejercutar el código.
            contador += 1 # Sumamos una unidad al contador, pues ya se ha mostrado una línea.
            if contador == 15: 
                break  # Detiene el ciclo después de 15 líneas.
        print(f"Se mostraron las primeras {contador} líneas del archivo.")


def CE():
    nombre_archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: datos.csv): ")  # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    ruta = "./Reto_Unidad_5/" + nombre_archivo  # Se ingresa la ruta del archivo, para leerlo correctamente.
    
    valores = []  # Se crea una lista vacía para almacenar los datos de la columna específica.
    
    with open(ruta, "r", encoding="latin-1") as archivo:  # Se abre el archivo de texto. Se usa encoding="latin-1" para asegurar que la información se interprete en el formato correcto.
        lector = csv.reader(archivo)  # Se usa el módulo csv para leer correctamente los datos separados por comas.
        columna = int(input("Ingrese el número de la columna que desea analizar (empezando desde 0): "))  # Permite elegir al usuario la columna a analizar.
        for fila in lector:  # Se usa un bucle for para recorrer cada fila del archivo.
            try:
                valor = float(fila[columna])  # Convierte el dato a número (float) para permitir operaciones matemáticas.
                valores.append(valor)  # Se agregan los datos a la lista.
            except (ValueError, IndexError):
                continue  # Ignora filas vacías o con datos no numéricos.
    
    n = len(valores)  # Se define una variable para contar cuántos valores tiene la lista, es decir, con cuántos datos se van a calcular las estadísticas.
    
    # Se calcula el promedio.
    suma = 0
    for v in valores:
        suma += v
    promedio = suma / n
    
    # Se calcula la mediana.
    valores_ordenados = sorted(valores)  # sorted() permite organizar los datos de menor a mayor, paso estrictamente necesario para calcular la mediana.
    if n % 2 == 0:
        mediana = (valores_ordenados[n//2 - 1] + valores_ordenados[n//2]) / 2  # Si el número de valores es par, indica que la mediana va a estar dada por el promedio de dos valores. Si es impar, va a ser un único elemento.
    else:
        mediana = valores_ordenados[n//2]
    
    # Se calcula la desviación estándar.
    suma_diferencias = 0
    for v in valores:
        suma_diferencias += (v - promedio) ** 2
    desviacion = (suma_diferencias / n) ** 0.5
    
    maximo = max(valores)
    minimo = min(valores)
    
    print(f"=== CALCULOS ESTADÍSTICOS ===\n Número de Datos ---> {n}\n Promedio ---> {promedio}\n Mediana ---> {mediana}\n Desviación Estándar ---> {desviacion}\n Máximo ---> {maximo}\n Mínimo ---> {minimo}")

    # Se retornan los resultados en forma de diccionario, para poder mostrarlos después.
    return {
        "Número de datos": n,
        "Promedio": promedio,
        "Mediana": mediana,
        "Desviación estándar": desviacion,
        "Máximo": maximo,
        "Mínimo": minimo
    }
# ¡DECLARACIÓN DE IA! En esta función, se le preguntó como hacer que se ignoraran filas que no contuvieran datos numéricos. Sugirió usar "try, except".
# ¡DECLARACIÓN DE IA! Se usó para calcular la desviación estándar con los datos.

def GUCCLD():      
    nombre_archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: datos.csv): ") # Pedimos al usuario el nombre del archivo junto con su extensión para trabajar sobre él.
    delimitador = input("¿Su archivo está delimitado por ',' ó ';')? Digite su respuesta: ") # Se pide especificar qué tipo de delimitador tiene el archivo para procesarlo correctamente.
    columna = input("Ingrese el nombre de la columna a graficar: ") # Así podemos saber cuáles son los datos de la columna de interés.
    ruta = "./Reto_Unidad_5/" + nombre_archivo # Se ingresa la ruta del archivo, para leerlo correctamente.
    with open(ruta, "r", encoding='latin-1') as archivo: # Se abre el archivo de texto. Se usa encoding="latin-1" para asegurar que la información se interprete en el formato correcto.
        lector = csv.DictReader(archivo, delimiter = delimitador) # csv.DictReader permite interpretar cada fila del archivo como un diccionario. También se especifica el delimitador ya concocido.
        # ¡DECLARACIÓN DE IA! Se hizo uso de IA para conocer el módulo csv.DictReader que es muy conveniente para esta función.
        datos = [] # Se crea una lista vacía.
        for fila in lector: # Se usa el bucle for para recorrer cada fila.
            valor = fila[columna] # Extraemos los datos de cada fila ubicados en una colunma en específico. 
            datos.append(float(valor)) # Se agregan los datos ya extraidos a la lista.
        if datos: # Se ejecuta siempre que la lista datos no esté vacía.
            x = [] # Lista vacía para variable x (abscisas) en el gráfico.
            y = [] # Lista vacía para variable y (ordenadas) en el gráfico.
            for i in range(len(datos)): # Se ejecuta tantas veces como datos hayan.
                x.append(i) # Para cada posición...
                y.append(datos[i]) # ...corresponde un dato.
            plt.scatter(x, y) # Se dibuja una gráfica de puntos que toma los valores de X como eje horizontal, los valores de Y como eje vertical.
            plt.title(f'Gráfico de la columna: {columna}') # Se agrega un título al gráfico.
            plt.xlabel('Índice') # Nombra al eje. 
            plt.ylabel(columna) # Nombra al eje.
            plt.show() # Muestra al gráfico en pantalla.
        else:
            print("No se encontraron datos numéricos en esa columna.")      
 


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
            OPCION3 = int(input("Ha seleccionado la opción que le permite procesar archivos (.csv).\n Esta opción le permite: \n (1). Mostrar las 15 primeras filas.\n (2). Calcular estadísticas.\n (3). Graficar una columna completa con los datos.\n (4). Salir.\n Ahora, seleccione qué desea realizar con su archivo: "))
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

