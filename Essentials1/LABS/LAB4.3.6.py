#Tu tarea es escribir y probar una función que toma tres argumentos 
# (un año, un mes y un día del mes) y devuelve el día correspondiente del año, 
# o devuelve None si cualquiera de los argumentos no es válido.

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #lista base de los dias de cada mes
    if is_year_leap(year) and month == 2:#solo si es bisiesto y es febrero se retorna algo diferente a lo de la lista
        return 29
    return month_days[month - 1]

def number_of_day_of_year(year, month, day):
    days = 0
    #primer for es para calcular la totalidad de los dias de los meses anteriores
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    #calculo la cantidad de dias en el mes enviado
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day #devuelve la suma de los dias anteriores mas el dia enviado por parametro
    else:
        return None #cubre casos de parametros incorrectos


def cuantos_dias_con_Bri(nosConocimos, diaHoy):
    stmnt = print("Llevamos esta cantidad de dias amandonos: ", diaHoy - nosConocimos)
    return stmnt

# print(number_of_day_of_year(2025, 8, 4))

cuantos_dias_con_Bri(number_of_day_of_year(2025, 2, 8), number_of_day_of_year(2025, 8, 4))#tambien puedo pasar funciones como paramentros