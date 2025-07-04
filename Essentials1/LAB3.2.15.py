# hipotesis de collatz 
# el proceso es que si un numero es par se divide por 2 y si es impar se multiplica por 3 y se le suma 1, eventualmente todo numero llegara a 1
# el programa debe:
# Leer un número natural c0.
# Aplicar el proceso anterior repetidamente hasta que c0 == 1.
# Mostrar cada nuevo valor de c0 en pantalla.
# Contar cuántos pasos tomó llegar a 1.
# Mostrar ese conteo al final.

  
steps = 0
c0 = int(input("Ingrese un número: "))
while c0 != 1:
    if c0 % 2 == 0: # si c0 es par
        c0 = c0 // 2
        steps += 1
        print(c0)
    else:
        c0 = c0 * 3 + 1
        steps += 1
        print(c0)
print(f"Tomaron {steps} pasos para llegar a {c0}")