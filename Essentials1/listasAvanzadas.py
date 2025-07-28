# procedemos a entender la comprension de listas
# la comprension de listas es una herramienta que nos permite crear listas de manera facil
# sintaxis de la comprension de listas
# mylist = [Mass variable + limitation statement]

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers] #este es creado en base a variables de un arreglo
print(squared_numbers)

squares = [x ** 2 for x in range(5)] #este es creado en base a indices
print(squares)

#este ejemplo llamaemoslo  con condicion limitante anidada
# ya que es un if dentro de un for
odds = [x for x in squares if x % 2 != 0] #este es crea lista solo de valores impares de squares
print(odds)



######ARREGLOS BIDIMENSIONALES o MATRICES#######
#matrices son listas de listas 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

