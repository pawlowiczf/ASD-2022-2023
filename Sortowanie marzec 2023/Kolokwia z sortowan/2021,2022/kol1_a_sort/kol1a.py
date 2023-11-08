from kol1atesty import runtests


def equal(p,q):
    if p == q or p == q[::-1]: return 1
    return 0

# def counting_sort(A,k,p):
#     C = [0] * k
#     B = [0] * len(A)
#     for i in range( len(A) ):
#         C[ ord(A[i][p]) ] += 1
#     # Tablica C zawiera ilosc wystapien danego elementu w tablicy A 

#     for i in range(1, k ):
#         C[i] = C[i] + C[i-1]
#     # Tablica C zawiera teraz ilosc liczb poprzedzajacych i wraz z nimi

#     for i in range( len(A) - 1, -1, -1 ): # przez to ze idziemy od konca mamy stabilnosc
#         B[ C[ ord(A[i][p]) ] - 1 ] = A[i]
#         C[ ord(A[i][p]) ] -= 1

#     for i in range(len(A)):
#         A[i] = B[i]
    
# #end def ^^^

# def radix_sort(A):
#     #
#     for p in range( 3, -1, -1 ):
#         counting_sort(A, 150, p)


def counting_sort(A,k,p):
    C = [0] * k
    B = [0] * len(A)
    for i in range( len(A) ):
        if p >= len( A[i] ): C[ 0 ] += 1
        else: C[ ord(A[i][p]) ] += 1
    # Tablica C zawiera ilosc wystapien danego elementu w tablicy A 

    for i in range(1, k ):
        C[i] = C[i] + C[i-1]
    # Tablica C zawiera teraz ilosc liczb poprzedzajacych i wraz z nimi

    for i in range( len(A) - 1, -1, -1 ): # przez to ze idziemy od konca mamy stabilnosc

        if p >= len( A[i] ):
            B[ C[ 0 ] - 1 ] = A[i]
            C[ 0 ] -= 1
        else:
            B[ C[ ord(A[i][p]) ] - 1 ] = A[i]
            C[ ord(A[i][p]) ] -= 1
    #

    for i in range(len(A)):
        A[i] = B[i]
    
#end def ^^^

def radix_sort(A):
    #
    max_length = 0
    for i in range( len(A) ):
        if len( A[i] ) > max_length: max_length = len( A[i] )
    

    for p in range( max_length - 1, -1, -1 ):
        counting_sort(A, 135, p)



s = [ "pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]

radix_sort(s)
print(s)


    



# def g(T):
#     # tu prosze wpisac wlasna implementacje
#     return -1


# # Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
# runtests( g, all_tests=False )

