archivo = open("texto2.txt","r")
''' 
archivo.readline()
archivo.readline()
archivo.read(33)
'''
archivo.seek(4) # Solo funciona para mover el "cursor" desde el inicio. 
datos = archivo.readline()
archivo.close()

print (datos)
