import shutil
import zipfile
import zipfile
import datetime

#cadena = "BDD34__OPERADORES.zip"
#fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
fecha_actual = datetime.datetime.now().strftime("%d")
dia_anterior = datetime.date.today() - datetime.timedelta(days=1)
#se toma solo el dia y no la fecha completa
ayer = (dia_anterior.strftime('%d'))


#reescalados

jungle_zip = zipfile.ZipFile('D:\Informes\Control del Churn\\2023\BDD40_MayoPendientes_PQR_reescalados.zip', 'w')
jungle_zip.write('D:\Informes\Control del Churn\\2023\BDD40_MayoPendientes_PQR_reescalados.xls', compress_type=zipfile.ZIP_DEFLATED)



from tkinter import messagebox
messagebox.showinfo(message="hola joven anzola se comprimieron los archivos, gracias  ", title="Título")