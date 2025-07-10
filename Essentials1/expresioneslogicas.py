 # Ejemplo 1:

var = 1
print(var > 0) # true
print(not (var <= 0)) # true
 
 
# Ejemplo 2:
print(var != 0) # true
print(not (var == 0)) # true

# ejemplo 3:
i = 1
j = not not i
print(" jota : ",j)

# ejemplo 4:
i = 15
j = 22

log = i and j
print("operacion a nivel logico: ",log)
bit = i & j
print("operacion a nivel bit: ",bit) #el resultado sera 6 ya que con operadores bit a bit hace comparacion 
                                     #de bits y devolvera el numero decimal resultante de la operacion

logneg = not i
print("operacion a nivel logico: ",logneg)
bitneg = ~i
print("operacion a nivel bit: ",bitneg)



