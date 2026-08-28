def binarysearch(arr, item):
    low = 0
    high = len(arr)-1
    steps=0

    while low<=high:
        mid=(low+high)//2
        guess=arr[mid]
        if guess == item:
            steps+=1
            print(f"Paso {steps}\n")
            print(f"Pasos totales: {steps}\n")
            print(f"El valor se encuentra en la posicion: {mid}\n")
            return mid
        elif guess > item:
            steps+=1
            print(f"Paso {steps}")
            high = mid-1
        else:
            steps+=1
            print(f"Paso {steps}")
            low = mid+1
    print("No se encuentra en la lista")        
    return None

myList = [1,2,9,12,21,34,42,77,99,233,5324,42212]
# print(binarysearch(myList,99))
print(binarysearch(myList,233))
# con palabras
myWords = ["ana", "brittany", "bruno", "carlos", "diana", "elena", "fabio", "gloria", "hugo", "irene", "jorge", "julio"]
print(binarysearch(myWords,"brittany"))
