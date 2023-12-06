import openpyxl
import csv

# Abrir archivo de Excel
workbook = openpyxl.load_workbook('archivo.xlsx')
worksheet = workbook.active

# Abrir archivo de texto con columnas delimitadas por '|'
with open('archivo.txt', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for row in reader:
        # Seleccionar columna por coma
        column = row[0].split(',')
        print(column)

