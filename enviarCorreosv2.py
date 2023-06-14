import pydoc
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Credenciales de la cuenta de Office 365
username = 'jaimesle@globalhitss.com'
password = 'Incorrect@1'

# Configuración del servidor SMTP
smtp_server = 'smtp.office365.com'
smtp_port = 587

# Conexión a la base de datos de Office 365
cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=outlook.office365.com;'
                      'User ID=' + username + ';'
                      'Password=' + password + ';'
                      'Trusted_Connection=yes;')
cursor = cnxn.cursor()

# Consulta para obtener los destinatarios del correo electrónico
#query = 'SELECT Email FROM Contacts WHERE Categoria=\'Destinatarios\''
#cursor.execute(query)
destinatarios = 'luis.jaimess@claro.com.co'

# Creación del correo electrónico
msg = MIMEMultipart()
msg['From'] = username
msg['To'] = ', '.join(destinatarios)
msg['Subject'] = 'Prueba'

# Cuerpo del correo electrónico
body = 'Esto es una prueba'
msg.attach(MIMEText(body, 'plain'))

# Adjunto al correo electrónico
with open('ruta_del_archivo.pdf', 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='xls')
    attachment.add_header('Content-Disposition', 'attachment', filename='D:\Informes\Datos_personales')
    msg.attach(attachment)

# Envío del correo electrónico
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(username, destinatarios, msg.as_string())

# Cierre de la conexión a la base de datos
cnxn.close()
