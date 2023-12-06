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
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 01 Bases Normales\\2023\\12 Diciembre")

# #AJU
# shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_PQR_VS_AJU.zip", 
#             "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")

#IPC
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_QMF_Marcacion_CAN-IPC.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")

#AEC
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Marca_PQR_AEC.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")

#Fuera de horario
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Fuera_de_Horario.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")


#fms
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Marcacion_DIS-FMS.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")


#llamadas caidas
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_SIC_Llamadas_Caidas.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")

#usuario recursos
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Usuarios_Recursos.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")

#dth
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_DTH.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 03 Canal Telefonico\\2023\\12 Diciembre")

#Reincidencia PQR
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD31_Reincidencia_PQR.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")

#Ingresos pqr
shutil.copy("D:\Informes\BASES DIARIAS PQR\BDD_Ingresos_pqr_Dic_2023_0.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")
#Finalizados PQR
shutil.copy("D:\Informes\BASES DIARIAS PQR\BDD_Finalizados_Pqr_Dic_2023.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 31 PQR Operacional\\2023\\12 Diciembre")

#escala pymes
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Usuarios_Escala_Pymes.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\34 PQR Pymes Corporativo\\2023\\12 Diciembre")

#HFC
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_Pyme_HFC.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\34 PQR Pymes Corporativo\\2023\\12 Diciembre")

#CTR
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_CTR.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 01 Bases Normales\\2023\\12 Diciembre")

#ITA
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_Marca_ITA.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 01 Bases Normales\\2023\\12 Diciembre")

#Webcenter
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD13_Marcaciones_Webcenter.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Marcaciones\\2023\\12 Diciembre")

#GTC
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD23_MARCA_GTC.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 01 Bases Normales\\2023\\12 Diciembre")

#Escalados Vip_IVR
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Escalados_VIP_IVR.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 03 Canal Telefonico\\2023\\12 Diciembre")

#Reincidencia Vip_IVR
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD11_Reincidencia_VIP_AV.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 03 Canal Telefonico\\2023\\12 Diciembre")

#Marca DSS
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Marca_DIS_DSS.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 01 Bases Normales\\2023\\12 Diciembre")

#Inventario DSS
shutil.copy("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Inventario_DIS_DSS.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 01 Bases Normales\\2023\\12 Diciembre")

#Pendientes LOG
shutil.copy("D:\Informes\BDD31_PQR_Log_Pendientes.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 07 Bases de Datos\\30 PQR\\31 PQR Operacional\\2023\\12 Diciembre")

#Rescalados
shutil.copy("D:\Informes\Control del Churn\\2023\BDD40_DiciembrePendientes_PQR_reescalados.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 01 Tickets\\2023\\12 Diciembre")




# sirve para que muestre en pantalla un mensaje 
from tkinter import messagebox
messagebox.showinfo(message="hola joven luchito los archivos fueron publicados gracias  ", title="Título")
