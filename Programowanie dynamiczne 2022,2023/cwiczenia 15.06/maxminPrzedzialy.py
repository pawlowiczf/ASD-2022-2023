# Rozwazmy ciag (a0, . . . , an−1) liczb naturalnych. Załózmy, ze został podzielony
# na k spójnych podciagów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1). Przez wartosc i-go podciagu
# rozumiemy sume jego elementów a przez najgorszy podciag rozumiemy podciag o najmniejszej wartosci (rozstrzygajac
# remisy w dowolny sposób). Wartoscia podziału jest wartosc jego najgorszego podciagu. Zadanie
# polega na znalezienie podziału ciagu (a0, . . . , an−1) o maksymalnej wartosci.

# F(i, j, k) - minimalna suma podprzedzialu [i : j] w optymalnym podziale przedzialu
# [i : j] na k przedzialow (suma podciagu o najmniejszej sumie jest najwieksza)

# F(i, j, 1) = sum( T[i : j + 1] ) if k == 1 
# F(i, j, k) = max( F(m, j, k - 1) , suma(i, m) ) po m przedzaile (i + 1, j)
# F(i, j) = inf dla i > j 


def SumOfSubsequence(A):
    #
    size = len(A)
    ArraySum = [ [ 0 for _ in range(size) ] for _ in range(size) ]

    for a in range( size ):
        ArraySum[a][a] = A[a]

        for b in range(a + 1, size):
            ArraySum[a][b] += ArraySum[a][b - 1] + A[b]
    
    #end 'for' loops 

    return ArraySum
#end proceure SumOfSubsequence()


def Rek(A, F, SumArray, a, b, k):
    #
    if a > b: return -float('inf')
    if k == 1: return SumArray[a][b]

    if (a, b, k) not in F:
        bestPartition = -float('inf')

        for x in range(a + 1, b):
            bestPartition = max( bestPartition, min( SumArray[a][x], Rek(A, F, SumArray, x + 1, b, k - 1)  ) )
        #
        F[ (a, b, k) ] = bestPartition 
    #

    return F[ (a, b, k) ]
#end procedure Rek()  


def MinMax(A, k):
    #
    size = len(A) 
    n = len(A)

    F = {}
    SumArray = SumOfSubsequence(A)

    return Rek(A, F, SumArray, 0, n - 1, k)
#end procedure MinMax()


def MinMaxDP(A, k):
    #
    n = len(A)
    
    # F(x, k) - maksymalna suma minimalnego przedzialu ze zbioru [1, ..., x], wykorzystujac k przedzialow 
    F = [ [ -float('inf') for _ in range(k + 1) ] for _ in range(n) ]

    ArraySum = [ 0 for _ in range(n) ]

    F[0][1] = A[0]
    for a in range(1, n):
        F[a][1] = F[a - 1][1] + A[a]
    #

    ArraySum[0] = A[0]
    for a in range(1, n):
        ArraySum[a] += ArraySum[a - 1] + A[a] 
    #

    for partition in range(2, k + 1):
        for a in range(partition - 1, n): # ilosc elementow x, jesli dzielimy na y przedzialow, musi byc x >= y
            for x in range(partition - 2, a):

                F[a][partition] = max( F[a][partition], min( F[x][partition - 1], ArraySum[a] - ArraySum[x] ) )
    #

    return F[n - 1][k]
#end proceure MinMaxDP()



A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
print( MinMax(A, 3) ) # 13
print( MinMaxDP(A, 3) ) 
print()

A = [5, 6, 1, 3, 12, 1, 6, 5, 8, 2, 7]
print( MinMax(A, 3) ) # 15
print( MinMaxDP(A, 3) ) 
print()

A = [ 5, 7, 4, 2, 8, 1, 6 ] 
print( MinMax(A, 3) ) # 7
print( MinMaxDP(A, 3) ) 
print()

A = [ 6, 5, 3, 8, 9, 10, 4, 7, 10 ]
print( MinMax(A, 4) ) # 14
print( MinMaxDP(A, 4) ) 
print()

