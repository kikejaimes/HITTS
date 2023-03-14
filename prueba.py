import shutil
import os
import datetime


fecha_actual = datetime.datetime.now().strftime("%d")
archivo = (f"BDD34_{fecha_actual}_OPERADORES.zip")
origen = os.path.join("D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos",archivo)
destino = os.path.join("C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 2023\\03 Marzo")



shutil.copy(origen, destino)
