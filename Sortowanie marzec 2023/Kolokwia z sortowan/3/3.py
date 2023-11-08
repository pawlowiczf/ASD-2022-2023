import math


def insertionSort(T):
    n = len(T)
    #
    for i in range(1, n):
        j = i
        while j > 0 and T[ j - 1 ][1] > T[ j ][1]:
            T[j-1], T[j] = T[j], T[j-1]
            j = j - 1
        #
    #end for
#end def ^^^



def bucketSort(T):
    n = len(T)
    buckets = [ [] for i in range(n) ]
    
    for i in range( n ):
        index = int( T[i][1] * n )
        buckets[ index ].append ( T[i] )
    #

    for i in range( len(buckets) ):
        insertionSort( buckets[i] )
    #
    result = []
    for i in range( len( buckets ) ):
        for j in range( len( buckets[i] ) ):
            result.append( buckets[i][j][0] )
    #end for
    return result
#end def ^^^



def FastSort(T,a):
    n = len(T)
    #
    for i in range( n ):
        T[i] = ( T[i], math.log( T[i] ) / math.log( a ) )
    #
    result = bucketSort(T)
    return result
#end def ^^^

T = [ 1.4142, 1.51572, 1.7411, 1.07177, 1.1487, 1.23114, 1.31951, 1.4142, 1.51572, 1.6245, 1.7411, 1.86607 ]
T = FastSort(T, 2)
print(T)