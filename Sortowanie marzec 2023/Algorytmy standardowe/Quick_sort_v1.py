def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    #end for
    array[i+1], array[high] = array[high], array[i+1]

    return i + 1 

def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)

#end def



T = [10, 7, 8, 9, 1, 5]
quicksort(T, 0, len(T) - 1)
print(T)
