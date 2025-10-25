# Aplicación CLI (Command Line Interface) de análisis y graficación de datos.

# Creación de funciones CASE 2 MENÚ PRINCIPAL:

def CNPYC():
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión, por ejemplo: texto.txt): ")
    archivo = open(nombre_archivo, "r", encoding="utf-8") # Se abre el archivo de texto.
    contenido = archivo.read()
    num_palabras = len(contenido.split()) # Se cuenta el número de palabras.
    num_caracteres_total = len(contenido) # Se lee el número de caracteres.
    num_caracteres_sin_espacios = len(contenido.replace(" ", "").replace("\n", "")) # Se lee la cantidad de caracteres, sin incluir los espacios.
    print("=== RESULTADOS ===")
    print(f"Archivo: {nombre_archivo}")
    print(f"Número de palabras: {num_palabras}")
    print(f"Caracteres totales (incluyendo espacios): {num_caracteres_total}")
    print(f"Caracteres sin espacios: {num_caracteres_sin_espacios}")

def RUPPO():
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión, por ejemplo: texto.txt): ")
    archivo = open(nombre_archivo, "r", encoding="utf-8") # Se abre el archivo de texto.
    contenido = archivo.read()
    palabra_buscar = input("Ingrese la palabra que desea reemplazar: ")
    palabra_reemplazo = input("Ingrese la nueva palabra: ")
    ocurrencias = contenido.count(palabra_buscar) # Permite contar cuántas veces aparece antes de reemplazar
    if ocurrencias == 0:
        print(f"La palabra '{palabra_buscar}' no se encontró en el archivo.")
    else:
        nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazo) # Se reemplaza la palabra.
        with open(nombre_archivo, "w", encoding="utf-8") as archivo: # Guardar cambios sobrescribiendo el archivo. Se usa utf-8 para evitar problemas con tiles y letras "ñ".
            archivo.write(nuevo_contenido)
        print("=== REEMPLAZO COMPLETADO CON ÉXITO ===")
        print(f"Archivo: {nombre_archivo}")
        print(f"Palabra reemplazada: '{palabra_buscar}' ---> '{palabra_reemplazo}'")
        print(f"Ocurrencias reemplazadas: {ocurrencias}")

# Creación de funciones CASE 3 MENÚ PRINCIPAL:

def M15PF ():
    nombre_archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: datos.csv): ")
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    print("=== PRIMERAS QUINCE (15) FILAS DEL ARCHIVO ===")
    contador = 0
    for linea in archivo:
        print(linea.strip())  # elimina los saltos de línea
        contador += 1
        if contador == 15:
            break  # detiene el ciclo después de 15 líneas
    archivo.close()
    print(f"Se mostraron las primeras {contador} líneas del archivo.")

def CE():
    nombre_archivo = input("Ingrese el nombre del archivo CSV (por ejemplo: datos.csv): ")
    columna = int(input("Ingrese el número de la columna que desea analizar (empezando desde 0): "))
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    datos = []
    contador = 0
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        # Se ignora la primera línea si tiene encabezados
        if contador == 0:
            contador += 1
            continue
        if columna < len(partes):
            valor = partes[columna]
            # Solo se agregan valores numéricos
            if valor.replace('.', '', 1).isdigit():
                datos.append(float(valor))
        contador += 1
    archivo.close()
    # Verificar que haya datos
    n = len(datos)
    if n == 0:
        print("No hay datos numéricos en esa columna.")
        return None
    # Calcular promedio
    suma = 0
    for v in datos:
        suma += v
    promedio = suma / n
    # Calcular mediana
    datos.sort()
    if n % 2 == 0:
        mediana = (datos[n//2 - 1] + datos[n//2]) / 2
    else:
        mediana = datos[n//2]
    # Calcular desviación estándar
    suma_cuadrados = 0
    for v in datos:
        suma_cuadrados += (v - promedio) ** 2
    desviacion = (suma_cuadrados / n) ** 0.5
    maximo = datos[-1]
    minimo = datos[0]
    return n, promedio, mediana, desviacion, maximo, minimo


def HDODLV():
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
                    print ("Aún se está trabajando en la función.")
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
                    HDODLV()
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

