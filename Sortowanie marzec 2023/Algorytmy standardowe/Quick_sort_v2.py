# Podejrzewam, ze dobrze dziala

def partition(array, low, high):
    i = low
    j = high - 1
    pivot = array[high]

    while i < j:
        while i < high and array[i] < pivot:
            i += 1
        while j > low and array[j] >= pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[high] = array[high], array[i]
    #end while
    return i 

def quicksort(T, low, high):
    if low < high:
        pivot = partition(T, low, high)
        quicksort(T, low, pivot - 1)
        quicksort(T, pivot + 1, high)

#end def


T = [5,3,9,1,4,6, -100]
quicksort(T, 0, len(T) - 1)
print(T)
