# # find the biggest square i can divide a land
# dara 10m porque siempre el mayor comun denominador podra no ser menos de 1 
# height = 7530
# width = 29650

# def findBiggestSquare(a,b):
#     if(b==0):
#         return a
#     return findBiggestSquare(b, a%b)

# biggest = findBiggestSquare(width, height)
# print(f"La caja mas grande que puede hacer es de {biggest}x{biggest}mts.")
# find the biggest square i can divide a land
height = 640
width = 1680

def findBiggestSquare(a,b):
    if(b==0):
        return a
    return findBiggestSquare(b, a%b)

biggest = findBiggestSquare(width, height)
print(f"La caja mas grande que puede hacer es de {biggest}x{biggest}mts.")

