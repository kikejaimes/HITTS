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


#metodo 2 funcionando 
# origen = "D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\Python\BDD88_17_Inventario_DIS_DSS"
# destino = "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 2023 (1)"

# shutil.copytree(origen, destino)

#-----------------------------------------------------------

#funcionando 2023 
#shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_19_PQR_VS_AJU.zip", "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 2023 (1)\\02 FEBRERO")

#----------------------------------------------------------------------------

#CRC
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31__QMF_Marcacion_CAN-IPC-CRC.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\20 Fidelización y Retención\\23 Retencion\\01 Bases Normales\\2023\\06 Junio")

#AJU
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_PQR_VS_AJU.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\31 PQR Operacional\\2023\\06 Junio")

#IPC
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_QMF_Marcacion_CAN-IPC.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\31 PQR Operacional\\2023\\06 Junio")

#AEC
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Marca_PQR_AEC.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\31 PQR Operacional\\2023\\06 Junio")

#Fuera de horario
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Fuera_de_Horario.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\31 PQR Operacional\\2023\\06 Junio")


#fms
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Marcacion_DIS-FMS.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\31 PQR Operacional\\2023\\06 Junio")


#llamadas caidas
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_SIC_Llamadas_Caidas.zip", 
             "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\31 PQR Operacional\\2023\\06 Junio")

#usuario recursos
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Usuarios_Recursos.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\31 PQR Operacional\\2023\\06 Junio")

#dth
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_DTH.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\10 Centros de Contacto y Solucion\\11 Centros Telefónicos\\03 Canal Telefonico\\2023")

#Reincidencia PQR
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Reincidencia_PQR.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\06 Junio")

#Ingresos pqr
shutil.copy("D:\Informes\BASES DIARIAS PQR\BDD_Ingresos_pqr_Jun_2023_0.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\06 Junio")
#Finalizados PQR
shutil.copy("D:\Informes\BASES DIARIAS PQR\BDD_Finalizados_Pqr_Jun_2023.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\06 Junio")

#escala pymes
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Usuarios_Escala_Pymes.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\34 PQR Pymes Corporativo\\2023\\06 Junio")

#HFC
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Pyme_HFC.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\34 PQR Pymes Corporativo\\2023\\06 Junio")

#CTR
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_CTR.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\20 Fidelización y Retención\\23 Retencion\\01 Bases Normales\\2023\\06 Junio")

#ITA
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_Marca_ITA.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\20 Fidelización y Retención\\23 Retencion\\01 Bases Normales\\2023\\06 Junio")

#Webcenter
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD13_Marcaciones_Webcenter.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\10 Centros de Contacto y Solucion\\11 Centros Telefónicos\\07 Marcaciones\\2023\\06 Junio")

#GTC
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_GTC.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\20 Fidelización y Retención\\23 Retencion\\01 Bases Normales\\2023\\06 Junio")

#Escalados Vip_IVR
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_VIP_IVR.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\10 Centros de Contacto y Solucion\\11 Centros Telefónicos\\03 Canal Telefonico\\2023")

#Reincidencia Vip_IVR
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Reincidencia_VIP_AV.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\10 Centros de Contacto y Solucion\\11 Centros Telefónicos\\03 Canal Telefonico\\2023")

#Marca DSS
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Marca_DIS_DSS.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\20 Fidelización y Retención\\23 Retencion\\01 Bases Normales\\2023\\06 Junio")

#Inventario DSS
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Inventario_DIS_DSS.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\20 Fidelización y Retención\\23 Retencion\\01 Bases Normales\\2023\\06 Junio")

#Pendientes LOG
shutil.copy("D:\Informes\BDD31_PQR_Log_Pendientes.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\10 Centros de Contacto y Solucion\\11 Centros Telefónicos\\03 Canal Telefonico\\2023\\06 Junio")


# sirve para que muestre en pantalla un mensaje 
from tkinter import messagebox
messagebox.showinfo(message="hola joven anzola los archivos fueron publicados gracias  ", title="Título")
