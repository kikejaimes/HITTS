import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Configuración de la cuenta de correo
remite = 'jaimesle@globalhitss.com'
clave = 'Incorrect@1'
destinatario = 'luis.jaimess@claro.com.co'

# Configuración del servidor SMTP
servidor_smtp = 'smtp.outlook.office365.com'
puerto_smtp = 587

# Ruta de la plantilla de correo electrónico y el archivo a adjuntar
ruta_plantilla = 'D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Envio Correos\Plantillas\Diario\Base AJU VS PQR.oft'
#ruta_archivo = 'D:\Repositorio_PQR - Triara\PQR\Bases_Diarias\Archivos\BDD88_Inventario_DIS_DSS.zip'

# Leer la plantilla de correo electrónico
with open(ruta_plantilla,encoding="Latin-1",) as archivo:
    plantilla = archivo.read()

# Crear el mensaje de correo electrónico
mensaje = MIMEMultipart()
mensaje['From'] = remite
mensaje['To'] = destinatario
mensaje['Subject'] = 'PRUEBA'

# Agregar la plantilla de correo electrónico como parte del mensaje
mensaje.attach(MIMEText(plantilla, 'html'))

# Agregar el archivo adjunto al mensaje
#with open(ruta_archivo, 'rb') as archivo:
    #adjunto = MIMEApplication(archivo.read(), _subtype='zip')
    #adjunto.add_header('Content-Disposition', 'attachment', filename=os)
