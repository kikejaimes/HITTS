# mi_lista = ['enrique','laura','juan','carmen','william','leonidas']
# print(mi_lista[0])     
# print(mi_lista[1])
# print(mi_lista[2])
# print(mi_lista[3])
# print(mi_lista[4])
# print(mi_lista[5])




# a=4
# b=34

# print(a+b)

from datetime import datetime
from datetime import timedelta
import datetime

fecha_actual = datetime.datetime.now().strftime("%d")
dia_anterior = datetime.date.today() - datetime.timedelta(days=1)
ayer = (dia_anterior.strftime('%d'))





