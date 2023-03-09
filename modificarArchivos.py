from gettext import install
import pip
import openpyxl


pip install openpyxl

import openpyxl

# Abrir el archivo de Excel existente
workbook = openpyxl.load_workbook('nombre_del_archivo.xlsx')

# Seleccionar una hoja de trabajo específica
worksheet = workbook['nombre_de_la_hoja']

# Modificar una celda específica
worksheet['A1'] = 'Nuevo valor'

# Guardar los cambios en el archivo
workbook.save('nombre_del_archivo_modificado.xlsx')