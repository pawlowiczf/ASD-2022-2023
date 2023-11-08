from zad3testy import runtests



def insertionSort(T):
    n = len(T)
    #
    for i in range( 1, n ):
        j = i
        while j > 0 and T[j-1] > T[j]:
            T[j-1], T[j] = T[j], T[j-1]
            j -= 1
        #
    #end for
#end def ^^^

def bucketSort(T):
    n = len(T)
    maxValue = max( T ) + 10
    minValue = min( T )
    rangeBucket = ( maxValue - minValue ) / n
    #
    buckets = [ [] for _ in range(n)  ]
    for i in range( n ):
        index = int( ( T[i] - minValue ) / rangeBucket )
        buckets[ index ].append( T[i] )
    #
    for i in range( n ):
        insertionSort( buckets[i] )
    #
    result = []
    for i in range( n ):
        for j in range( len( buckets[i] ) ):
            result.append( buckets[i][j] )
    #
    return result
#end def ^^^
    

def bucketSort_2(T):
    n = len(T)
    maxValue = max( T )
    #
    for i in range(n):
        T[i] = (T[i], T[i] / maxValue)
    #
    buckets = [ [] for _ in range( n + 1 ) ]
    #
    for i in range( n ):
        index = int( n * T[i][1] )
        buckets[ index ]. append( T[i][0] )
    #
    for i in range( len(buckets) ):
        insertionSort( buckets[i] )
    #
    result = []
    for i in range( n + 1 ):
        for j in range( len( buckets[i] ) ):
            result.append( buckets[i][j] )
    #
    return result


def SortTab(T,P):
    T = bucketSort_2(T)
    return T
    

# runtests( SortTab )

T = [5.2, 2.7, 6.6, 3.9, 1.4, 4.8, 6.3, 7.0, 6.4, 1.1, 7.4, 5.4, 5.1, 4.3, 6.7, 7.2, 5.6, 7.7, 6.9, 1.6, 2.7, 4.1, 4.3, 6.5] 
T = bucketSort_2(T)
print(T)