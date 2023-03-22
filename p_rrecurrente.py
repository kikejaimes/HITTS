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

# operadores
shutil.copy(f"D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD34_{fecha_actual}_OPERADORES.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 2023\\03 Marzo")

#pendientes comprime y publica

jungle_zip = zipfile.ZipFile(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD31_{fecha_actual}_PENDIENTES.zip', 'w')
jungle_zip.write(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD31_{fecha_actual}_PENDIENTES.csv', compress_type=zipfile.ZIP_DEFLATED)

#marcaciones Cun
shutil.copy(f"D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD_Marcaciones_CUN.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 2023 (2)\\marzo")

#pend_sop
shutil.copy(f"D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD_PQRs_pend_Sop_{fecha_actual}_Marzo.zip", 
           "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 2023 (2)\\marzo")


from tkinter import messagebox
messagebox.showinfo(message="hola joven anzola los archivos fueron publicados gracias  ", title="Título")