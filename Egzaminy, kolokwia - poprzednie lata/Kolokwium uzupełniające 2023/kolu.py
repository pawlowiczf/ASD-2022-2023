from kolutesty import runtests

def Merge(T1, T2):
    #
    n1 = len(T1)
    n2 = len(T2)
    a, b = 0, 0 
    T = [ 0 for _ in range(n1 + n2) ]

    while a < n1 and b < n2:
        if T1[a] < T2[b]:
            T[a + b] = T1[a]
            a += 1 
        
        else:
            T[a + b] = T2[b] 
            b += 1
    #

    while a < n1:
        T[a + b] = T1[a] 
        a += 1 
    #

    while b < n2:
        T[a + b] = T2[b] 
        b += 1 
    #

    return T 
#end procedure Merge()

def MergeSort(T):
    #
    if len(T) > 1:
        middle = len(T) // 2

        T1 = T[0 : middle]
        T2 = T[middle : len(T)]
        T1 = MergeSort(T1)
        T2 = MergeSort(T2)

        T  = Merge(T1, T2)
    #

    return T 
#end procedure MergeSort()

def Partition(T, left, right):
    #
    a = left - 1

    for b in range(left, right):
        if T[b] <= T[right]:
            a += 1
            T[b], T[a] = T[a], T[b] 
    #

    a += 1
    T[a], T[right] = T[right], T[a] 
    return a 
#end procedure Partition()


def quickSort(T, left, right):
    #
    if left < right:
        pivot = Partition(T, left, right)
        quickSort(T, left, pivot - 1)
        quickSort(T, pivot + 1, right)
    #
#end procedure quickSort()


def ice_cream( T ):
    #
    quickSort(T, 0, len(T) - 1)
    # T = MergeSort(T)
    a = len(T) - 1
    maxVolume = 0
    time = 0

    while a >= 0 and T[a] - time > 0:
        maxVolume += T[a] - time 
        a -= 1 
        time += 1
    #

    return maxVolume
#end procedure ice_cream()

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )

