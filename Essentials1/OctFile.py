#En este codigo anterior estamos practicando condicionales if..elif..else

var=input("Que quieres decir...")

if var=="ESPATIFILO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif var=="espatifilo":
    print("No, ¡quiero un gran Espatifilo")
else:
    print("¡Espatifilo!, ¡No ",var+"!")
#################################################

ingreso=int(input("Ingresa tu ingreso: "))

if ingreso<85528:
    IPI=ingreso*0.18
    Total=IPI-556.2
    print("El impuesto total es de MXN$", round(Total,0))
else:
    excedente=ingreso-85528
    IPI=excedente*0.32
    Total=14839.2+IPI
    print("El impuesto total es de MXN$", round(Total,0))

##################################################
    
year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
	
