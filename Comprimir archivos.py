import zipfile
import zipfile


#CRC
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31__QMF_Marcacion_CAN-IPC-CRC.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31__QMF_Marcacion_CAN-IPC-CRC.xls', compress_type=zipfile.ZIP_DEFLATED)



#AJU
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_PQR_VS_AJU.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_PQR_VS_AJU.xls', compress_type=zipfile.ZIP_DEFLATED)

#Fuera de horario
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Fuera_de_Horario.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Fuera_de_Horario.csv', compress_type=zipfile.ZIP_DEFLATED)


#llamadas caidas
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_SIC_Llamadas_Caidas.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_SIC_Llamadas_Caidas.xls', compress_type=zipfile.ZIP_DEFLATED)

#Escala pymes
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Usuarios_Escala_Pymes.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Usuarios_Escala_Pymes.csv', compress_type=zipfile.ZIP_DEFLATED)

#HFC
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Pyme_HFC.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Pyme_HFC.csv', compress_type=zipfile.ZIP_DEFLATED)


#Webcenter
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD13_Marcaciones_Webcenter.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD13_Marcaciones_Webcenter.xls', compress_type=zipfile.ZIP_DEFLATED)

#GTC
#jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_GTC.zip', 'w')
#jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_GTC.csv', compress_type=zipfile.ZIP_DEFLATED)

#Escalados Vip_IVR
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_VIP_IVR.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_VIP_IVR.xls', compress_type=zipfile.ZIP_DEFLATED)

#Reincidencia Vip_AV
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Reincidencia_VIP_AV.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Reincidencia_VIP_AV.xls', compress_type=zipfile.ZIP_DEFLATED)



#Inventario DSS
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Inventario_DIS_DSS.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Inventario_DIS_DSS.csv', compress_type=zipfile.ZIP_DEFLATED)

#Usuario recurso
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Usuarios_Recursos.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Usuarios_Recursos.csv', compress_type=zipfile.ZIP_DEFLATED)


#Marca DISS DSS
jungle_zip = zipfile.ZipFile('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Marca_DIS_DSS.zip', 'w')
jungle_zip.write('D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Marca_DIS_DSS.csv', compress_type=zipfile.ZIP_DEFLATED)


#Descarga log
jungle_zip = zipfile.ZipFile('D:\Informes\BDD31_PQR_Log_Pendientes.zip', 'w')
jungle_zip.write('D:\Informes\BDD31_PQR_Log_Pendientes.csv', compress_type=zipfile.ZIP_DEFLATED)



from tkinter import messagebox
messagebox.showinfo(message="hola joven anzola se comprimieron los archivos, gracias  ", title="Título")