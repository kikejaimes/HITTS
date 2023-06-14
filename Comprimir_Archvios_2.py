import zipfile
import os

#Para comprimir archivos sin ruta absoluta se utiliza el os.path.basename  

# #CRC
with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31__QMF_Marcacion_CAN-IPC-CRC.zip', 'w') as archivo_zip:
     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31__QMF_Marcacion_CAN-IPC-CRC.xls', os.path.basename('BDD31__QMF_Marcacion_CAN-IPC-CRC.xls'), compress_type=zipfile.ZIP_DEFLATED)

# #AJU
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_PQR_VS_AJU.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_PQR_VS_AJU.xls', os.path.basename('BDD31_PQR_VS_AJU.xls'), compress_type=zipfile.ZIP_DEFLATED)

# #IPC
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_QMF_Marcacion_CAN-IPC.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_QMF_Marcacion_CAN-IPC.csv', os.path.basename('BDD31_QMF_Marcacion_CAN-IPC.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #AEC
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Marca_PQR_AEC.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Marca_PQR_AEC.csv', os.path.basename('BDD31_Marca_PQR_AEC.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #Fuera de horario
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Fuera_de_Horario.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Fuera_de_Horario.csv', os.path.basename('BDD31_Fuera_de_Horario.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #fms
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Marcacion_DIS-FMS.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Marcacion_DIS-FMS.csv', os.path.basename('BDD31_Marcacion_DIS-FMS.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #llamadas caidas
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_SIC_Llamadas_Caidas.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_SIC_Llamadas_Caidas.xls', os.path.basename('BDD31_SIC_Llamadas_Caidas.xls'), compress_type=zipfile.ZIP_DEFLATED)

#usuario recursos
with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Usuarios_Recursos.zip', 'w') as archivo_zip:
     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Usuarios_Recursos.csv', os.path.basename('BDD31_Usuarios_Recursos.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #dth
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_DTH.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_DTH.csv', os.path.basename('BDD11_Escalados_DTH.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #Reincidencia PQR
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Reincidencia_PQR.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Reincidencia_PQR.csv', os.path.basename('BDD31_Reincidencia_PQR.csv'), compress_type=zipfile.ZIP_DEFLATED)

#Ingresos pqr
with zipfile.ZipFile('D:\Informes\BASES DIARIAS PQR\BDD_Ingresos_pqr_Jun_2023_0.zip', 'w') as archivo_zip:
    archivo_zip.write('D:\Informes\BASES DIARIAS PQR\BDD_Ingresos_pqr_Jun_2023_0.xls', os.path.basename('BDD_Ingresos_pqr_Jun_2023_0.xls'), compress_type=zipfile.ZIP_DEFLATED)

#Finalizados PQR
with zipfile.ZipFile('D:\Informes\BASES DIARIAS PQR\BDD_Finalizados_Pqr_Jun_2023.zip', 'w') as archivo_zip:
    archivo_zip.write('D:\Informes\BASES DIARIAS PQR\BDD_Finalizados_Pqr_Jun_2023.xls', os.path.basename('BDD_Finalizados_Pqr_Jun_2023.xls'), compress_type=zipfile.ZIP_DEFLATED)

#escala pymes
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Usuarios_Escala_Pymes.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Usuarios_Escala_Pymes.csv', os.path.basename('BDD34_Usuarios_Escala_Pymes.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #HFC
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Pyme_HFC.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Pyme_HFC.csv', os.path.basename('BDD34_Pyme_HFC.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #CTR
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_CTR.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_CTR.csv', os.path.basename('BDD23_MARCA_CTR.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #ITA
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_Marca_ITA.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_Marca_ITA.csv', os.path.basename('BDD23_Marca_ITA.csv'), compress_type=zipfile.ZIP_DEFLATED)

#Webcenter
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD13_Marcaciones_Webcenter.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD13_Marcaciones_Webcenter.xls', os.path.basename('BDD13_Marcaciones_Webcenter.xls'), compress_type=zipfile.ZIP_DEFLATED)

# #GTC
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_GTC.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_GTC.csv', os.path.basename('BDD23_MARCA_GTC.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #Escalados Vip_IVR
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_VIP_IVR.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_VIP_IVR.xls', os.path.basename('BDD11_Escalados_VIP_IVR.xls'), compress_type=zipfile.ZIP_DEFLATED)

# #Reincidencia Vip_IVR
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Reincidencia_VIP_AV.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Reincidencia_VIP_AV.xls', os.path.basename('BDD11_Reincidencia_VIP_AV.xls'), compress_type=zipfile.ZIP_DEFLATED)

# #Marca DSS
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Marca_DIS_DSS.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Marca_DIS_DSS.csv', os.path.basename('BDD88_Marca_DIS_DSS.csv'), compress_type=zipfile.ZIP_DEFLATED)

# #Inventario DSS
# with zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Inventario_DIS_DSS.zip', 'w') as archivo_zip:
#     archivo_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Inventario_DIS_DSS.csv', os.path.basename('BDD88_Inventario_DIS_DSS.csv'), compress_type=zipfile.ZIP_DEFLATED)

# sirve para que muestre en pantalla un mensaje 
from tkinter import messagebox
messagebox.showinfo(message="hola joven anzola los archivos fueron publicados gracias  ", title="Título")
