# quicksort algorithm 
arreglo = [102,323,44,22,1,225,55663,563,2]
def quicksort(array):
    if (len(array)<2):
        return array
    else:
        pivot = array[0]
        lesserPivot = [i for i in array[1:] if i <= pivot]
        greaterPivot = [i for i in array[1:] if i > pivot]

        return quicksort(lesserPivot)+[pivot]+quicksort(greaterPivot) #[pivot] crea una lista de un dato

print(quicksort(arreglo))
