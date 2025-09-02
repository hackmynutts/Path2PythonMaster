hour = int(input("Hora de inicio (horas): "))#23
mins = int(input("Minuto de inicio (minutos): "))#58
dura = int(input("Duración del evento (minutos): "))#642

mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60
# encuentra el número de horas ocultas en los minutos y actualiza las horas
#en esta operacion, el resultado es 34 por el orden de prioridad del operador
##primero se va a hacer 1ero la // -> floor division
## hour = 23 + 700 // 60
## hour = 23 + 11 
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
#modulos o (%) es restar el divisor las veces que se pueda al dividendo
#y el sobrante es el resultado

print(hour, mins, sep=':')


