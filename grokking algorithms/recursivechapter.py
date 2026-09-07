# recursion es cuando una funcion se llama a si misma
# este caso es un caso NO DESEADO, ya que se ejecuta infinitamente porque no tiene un caso base


# def countdown(i):
#     print(i)
#     countdown(i-1)

# countdown(56)    

# con caso base
def countdown(i):
    print(i)
    if i <=0:
        print("Terminamos la recursividad con un caso base....!!!!")
        return
    else:
        countdown(i-1)

countdown(10)  

print("\n\n\n")




#Factorial con recursion
def factorial(x):
    print(f"El factorial de es: {x}")
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(13))