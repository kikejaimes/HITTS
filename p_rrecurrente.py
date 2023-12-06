import shutil
import zipfile
import zipfile
import datetime
import os


#para que se ejecute cada 2 horas

# import time
# def myfunction():
# # Haga algo aquí
# timer = time.Timer(120, myfunction)
# timer.start()




#cadena = "BDD34__OPERADORES.zip"
#fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
fecha_actual = datetime.datetime.now().strftime("%d")
dia_anterior = datetime.date.today() - datetime.timedelta(days=1)
#se toma solo el dia y no la fecha completa
ayer = (dia_anterior.strftime('%d'))

# operadores

#jungle_zip = zipfile.ZipFile(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD34_{fecha_actual}_OPERADORES.zip', 'w')
#jungle_zip.write(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD34_{fecha_actual}_OPERADORES.xls', compress_type=zipfile.ZIP_DEFLATED)

shutil.copy(f"D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD34_{fecha_actual}_OPERADORES.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 34 PQR Pymes Corporativo\\2023\\12 Diciembre")

#pendientes comprime y publica

jungle_zip = zipfile.ZipFile(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD31_{fecha_actual}_PENDIENTES.zip', 'w')
jungle_zip.write(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD31_{fecha_actual}_PENDIENTES.csv',os.path.basename('BDD31_{fecha_actual}_PENDIENTES.csv'),compress_type=zipfile.ZIP_DEFLATED)

shutil.copy(f"D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD31_{fecha_actual}_PENDIENTES.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")

# #marcaciones Cun
jungle_zip = zipfile.ZipFile(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD_Marcaciones_CUN.zip', 'w')
jungle_zip.write(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD_Marcaciones_CUN.xls',os.path.basename('BDD_Marcaciones_CUN.xls'), compress_type=zipfile.ZIP_DEFLATED)

shutil.copy(f"D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD_Marcaciones_CUN.zip", 
           "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 02 Marcaciones Diarias\\2023\\Diciembre")


#pend_sop

#jungle_zip = zipfile.ZipFile(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD_PQRs_pend_Sop_{fecha_actual}_Mayo.zip', 'w')
#jungle_zip.write(f'D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD_PQRs_pend_Sop_{fecha_actual}_Mayo.xls', compress_type=zipfile.ZIP_DEFLATED)

shutil.copy(f"D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD_PQRs_pend_Sop_{fecha_actual}_Diciembre.zip", 
          #"C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\40 Planeación y Estrategia\\41 Inteligencia de Clientes\\02 Gestion Informacion\\02 Marcaciones Diarias\\2023\\Diciembre")
           "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 02 Marcaciones Diarias\\2023\\Diciembre")

# #Ingresos O_virtuales

# jungle_zip = zipfile.ZipFile(f'D:\Informes\Oficinas_Virtuales\RepOp\\2023\BDD13_Ingresos_{fecha_actual}_Marzo_Oficinas_Virtuales.zip', 'w')
# jungle_zip.write(f'D:\Informes\Oficinas_Virtuales\RepOp\\2023\BDD13_Ingresos_{fecha_actual}_Marzo_Oficinas_Virtuales.csv', compress_type=zipfile.ZIP_DEFLATED)

# shutil.copy(f"D:\\OPERACION\\77-PENDIENTES_PQR_CUN_SOP\\files\BDD13_Ingresos_{fecha_actual}_Marzo_Oficinas_Virtuales.zip", 
#             "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 2023 (3)\\04 Abril")



# #Pendientes O_virtuales con fecha dia anterior
# shutil.copy(f"D:\Informes\Oficinas_ñVirtuales\RepOp\\2023\BDD13_{ayer}_Marzo_Pendientes_Oficinas_Virtuales.zip", 
#             "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 2023 (3)\\04 Abril")


from tkinter import messagebox
messagebox.showinfo(message="hola Luchito los archivos fueron publicados gracias  ", title="Título")