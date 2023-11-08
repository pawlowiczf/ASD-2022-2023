# Longest Increasing Subsequence
# Najdluzszy rosnacy podciag

"""
Funkcja F(i) zwraca dlugosc najdluzszego podciagu konczacego sie na indeksie 'i'.
F(i) = max( F(i), F(j): gdy j < i oraz A[j] < A[i] )
"""

def LongestIncreasingSubsequence(A):
    #
    n = len(A)

    # najdluzszy rosnacy podciag konczacy sie na indeksie i
    F = [ 1 for _ in range(n) ]
    P = [ None for _ in range(n) ]

    for i in range(1, n):
        for j in range(n):

            if A[i] > A[j] and F[j] + 1 > F[i]:
                P[i] = j
                F[i] = max( F[i], F[j] + 1 )
    #end for's 

    return restoreSubsequnce(A, F, P)
#end procedure LongestIncreasingSubsequence()


def restoreSubsequnce(A, F, P):
    #
    print( max(F) )
    index = F.index( max(F) )
    path = []

    while index != None:
        path.append( A[index] )
        index = P[index]
    #
    path.reverse()
    print(path)
    print()
#end procedure restoreSubsequence()


A = [ 3, 10, 2, 1, 20 ] # 3
LongestIncreasingSubsequence(A)  # 3 10 20

A = [ 50, 3, 10, 7, 40, 80 ] # 4
LongestIncreasingSubsequence(A)  # 3 7 40 80

A = [ 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 ] # 6
LongestIncreasingSubsequence(A)  # 0 2 6 9 13 15