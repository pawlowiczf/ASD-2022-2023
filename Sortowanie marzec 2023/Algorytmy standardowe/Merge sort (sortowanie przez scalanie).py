def mergeSort(array):

    if len(array) > 1:

        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        mergeSort(left_array)
        mergeSort(right_array)

        i = j = k = 0

        # Laczenie dwoch podtablic w jedna posortowana

        while i < len( left_array ) and j < len( right_array ):

            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            #end if
            k += 1
        #end while
        
        while i < len( left_array ):
            array[k] = left_array[i]
            i += 1
            k += 1
        #end while

        while j < len( right_array ):
            array[k] = right_array[j]
            j += 1
            k += 1
        #end while
#end def

T = [29,18,385,131,519,1319,-1,3,9,100]
mergeSort(T)
print(T)

