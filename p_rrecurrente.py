import shutil
import zipfile
import zipfile
import datetime

#cadena = "BDD34__OPERADORES.zip"
#fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
fecha_actual = datetime.datetime.now().strftime("%d")
# posicion = len(cadena) // 1

# cadena_nueva = cadena[:posicion] + fecha_actual + cadena[posicion:]

# print(cadena_nueva)



#'||trim(to_char(sysdate-1,'dd'))||'

#archivo = "BDD34_{fecha_actual}_OPERADORES.zip"

#Funcionando
shutil.copy(f"D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD34_{fecha_actual}_OPERADORES.zip", 
            "C:\\Users\jaimesle\Comunicacion Celular S.A.- Comcel S.A\Gerencia Cuidado al Cliente - 2023\\03 Marzo")

