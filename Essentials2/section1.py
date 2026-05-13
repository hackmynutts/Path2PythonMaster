import pandas, os, sys # tambien mas de un import a la vez
# from module import name as alias
from math import pi as π #ejemplo de alias para pi
# from math import * #importar todo el módulo math, aunque no es recomendado por posibles conflictos de nombres
import math as m #importar todo el módulo math
# todas estas son formas de importar módulos o partes de módulos en Python.

print(π) #imprime el valor de pi usando el alias
print(m.sqrt(16)) #imprime la raíz cuadrada de 16 usando el módulo math con el alias m
print(m.sin(m.pi/2)) #imprime el seno de pi/2 usando el módulo math con el alias m