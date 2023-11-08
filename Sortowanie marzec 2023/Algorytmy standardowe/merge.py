def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def merge2(T1, first, last, mid):
    
    i = first
    j = mid + 1
    T2 = []

    for k in range(first, last + 1):
        T2[k].append( T1[k] )
    
    for k in range(first, last + 1):

        if i > mid:
            T1[k] = T2[j]
            j += 1
        
        elif j > last:
            T1[k] = T2[i]
            i += 1

        elif T2[i] < T2[j]:
            T1[k] = T2[i]
            i += 1
        
        elif T2[i] >= T2[j]:
            T1[k] = T2[j]
            j += 1
        
    #end for
    return T1
#end def


def merge(T, l, p, mid):
    L = T[l:mid]
    P = T[mid:p+1]
    
    i = j = 0
    k = l

    while i < len(L) and j < len(P):
        if L[i] <= P[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = P[j]
            j += 1
        k += 1
    #end while

    while i < len(L):
        T[k] = L[i]
        i += 1
        k += 1
    while j < len(P):
        T[k] = P[j]
        j += 1
        k += 1
    
#end def


def merge_sort(T):
    def rek(T, l, p):
        if p - l < 1: return

        mid = (l + p) // 2
        rek(T, l, mid)
        rek(T, mid + 1, p)
        merge(T,l,p,mid)

    #end def
    rek(T, 0, len(T))
    return T
#end def

T = [3,6,19,1,4,23,16]

print( merge_sort(T) )



        