import csv
from itertools import zip_longest
import os

nueva = {"maxima":[], "debe": []}
busqueda = {"cedula": [], "curso": []}

with open('prueba.csv', newline='') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=';')  
    
    for row in reader:
        
        cedula = row[0]
        curso = row[1]
        
        busqueda['cedula'].append(cedula)
        busqueda['curso'].append(curso)

bbdd = {"cedula": [], "curso": [], "nota": []}

with open('bbdd.csv', newline='') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=';')  
    
    for row in reader:
        
        cedula = row[7]
        curso = row[3]
        nota = row[14]
        
        bbdd['cedula'].append(cedula)
        bbdd['curso'].append(curso)
        bbdd['nota'].append(nota)


####################################################################################################################

notas_correspondientes = []
for i in range(len(busqueda['cedula'])):
    cedula_busqueda = busqueda['cedula'][i].strip().lower()
    curso_busqueda = busqueda['curso'][i].strip().lower()
    notas_encontradas = []  
    for j in range(len(bbdd['cedula'])):
        cedula_bbbd = bbdd['cedula'][j].strip().lower()
        curso_bbbd = bbdd['curso'][j].strip().lower()
        if cedula_busqueda == cedula_bbbd and curso_busqueda == curso_bbbd:
            nota = bbdd['nota'][j]
            if nota != '-':
                notas_encontradas.append(int(nota))  
    if notas_encontradas:

        notas_correspondientes.append(max(notas_encontradas))
    else:
        #print("No se encontraron notas para cédula:", busqueda['cedula'][i], "y curso:", busqueda['curso'][i])
        notas_correspondientes.append(0)
        notas_encontradas.append("")

    try:
        maxima = max(notas_encontradas)
    except ValueError:
        pass
    #print("Notas encontradas para cédula:", busqueda['cedula'][i], "y curso:", busqueda['curso'][i], ":", notas_encontradas)
    nueva["maxima"].append(maxima)

####################################################################################################################

final = {"cedula": [], "curso": [], "nota": [], "Necesita?": []}
with open('prueba.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')  
    for row in reader:
        cedula = row[0]
        curso = row[1]
        final['cedula'].append(cedula)
        final['curso'].append(curso)
        final["nota"].append(notas_correspondientes.pop(0))

####################################################################################################################


notas= final["nota"]
for nota in notas:
    if nota>=80:
        debe = "No"
        nueva['debe'].append(debe)
        final['Necesita?'].append(debe)
    elif nota<80:
        debe = "Si"
        nueva['debe'].append(debe)
        final['Necesita?'].append(debe)

####################################################################################################################

with open('prueba.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    filas_modificadas = []
    for i, row in enumerate(reader):
        if i < len(nueva["maxima"]):  
            maxima = str(nueva["maxima"][i])  
            debe = nueva["debe"][i]           
            row.append(maxima)  
            row.append(debe)    
        filas_modificadas.append(row)

# Ahora puedes escribir las filas modificadas en un nuevo archivo CSV
with open('nuevo_prueba.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for row in filas_modificadas:
        writer.writerow(row)

print("Se ha creado un nuevo archivo 'nuevo_prueba.csv'")