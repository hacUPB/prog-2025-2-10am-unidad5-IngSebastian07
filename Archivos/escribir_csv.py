import csv

asignaturas = ["Propulsión", "Aerodinámica", "Control de vuelo", "Estructuras aeronáuticas", "Materiales compuestos", "Mecánica de fluidos"]

software = ["ANSYS", "NX", "MATLAB", "Python", "OpenVSP", "CATIA"]

numeros = [47, 12, 89, 63, 5, 78]


with open('C:\\Users\\USUARIO\\OneDrive\\Documentos\\Ingeniería Aeronáutica UPB\\S2 - Ingeniería Aeronáutica - UPB\\Programación\\Unidad_5\\prueba_escritura.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(asignaturas)  # Escribe la fila de encabezados
    escritor.writerow(software)
    escritor.writerow(numeros)
