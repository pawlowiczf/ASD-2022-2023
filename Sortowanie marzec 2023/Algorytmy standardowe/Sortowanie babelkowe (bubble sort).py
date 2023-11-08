from time import *
# Bardzo latwa zmiana sortowania malejaco/rosnaco ( zmiana znaku nierownosci w linijce 8,9 )

def bubble_sort( T ):
    n = len( T )

    for i in range(1,n): # element najmniejszy znajdzie sie od razu na indeksie 0, po pierwszym skonczeniu drugiej petli for 
        for j in range(n-1,i-1, -1):
            if T[j-1] > T[j]:
                T[j-1], T[j] = T[j], T[j-1]
        
        #end for 2
    #end for 1
    return T
#end def



def bubble_sort2( T ):
    n = len( T )
    sorted = False
    
    while not sorted:
        sorted = True 

        for i in range(0, n-1):
            if T[i] > T[i+1]: # jest to sortowanie stabilne, jesli wartosci sa rowne to sie nie zamienia
                sorted = False 
                T[i], T[i+1] = T[i+1], T[i]
        #end for 
    #end for
    return T
#end def



# T = [1,5,7,19,391,5,1,4,13,-13,-50]
# print( bubble_sort(T) )
# T = [1,5,7,19,391,5,1,4,13,-13,-50]
# print( bubble_sort2(T) )


print( bubble_sort(T) )

