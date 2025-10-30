# Primer Paso: Abrir el archivo y definir el modo.
archivo = open("texto.txt","r")
# Segundo Paso: Leer el archivo.
# datos = archivo.read(100) # Permite leer 10 caracteres del "archivo".
'''for i in range(5):
    datos = archivo.readline() # Lee los caracteres hasta que haya un "enter".
'''
'''for datos in archivo:
    print(datos[0]) # Imprime la línea cinco porque el "print()" no está dentro del "for".
'''

datos = archivo.readlines() # Lee todo el archivo como listas (cada línea es una lista), pero cada elemento de la lista es un string.
print(datos)
# Tercer Paso: Cerrar el archivo.
archivo.close()

# EOF significa End Of File. Es una constante que está escrita al final del archivo.
