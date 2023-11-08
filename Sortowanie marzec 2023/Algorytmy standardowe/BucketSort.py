# Liczby z zakresu [0,1], rozklad jednostajny


def insertion_sort(T):
    n = len(T)

    for j in range(1, n):
        i = j
        while T[i] < T[i-1] and i >= 1:
            T[i], T[i-1] = T[i-1], T[i]
            i -= 1
        #end while
    return T
#end def ^^^



# def BucketSort(T,n):
#     norm = max( T )
#     buckets = [ [] for i in range( n )]

#     for num in T:
#         norm_num = num / norm # normalized sum, norm_num jest teraz w przedziale [0,1]
#         buck_ind = int( n * norm_num )
#         buckets[ buck_ind ].append( num )
#     #

#     for i in range(n):
#         buckets[i] = insertion_sort( buckets[i] )
    
#     output = []
#     for i in range(n):
#         for j in range( len( buckets[i] ) ):
#             output.append( buckets[i][j] )
#     #end for
#     return T
# #end def ^^^


def BucketSort(T,n):
    buckets = [ [] for i in range( n )]

    for num in T:
        buck_ind = int( n * num )
        buckets[ buck_ind ].append( num )
    #

    for i in range(n):
        buckets[i] = insertion_sort( buckets[i] )
    
    output = []
    for i in range(n):
        for j in range( len( buckets[i] ) ):
            output.append( buckets[i][j] )
    #end for
    return output
#end def ^^^

T = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
T = BucketSort(T, 10)
print(T)