# https://github.com/MatiPl01/Algorytmy-i-struktury-danych/blob/master/Przydatne%20algorytmy/Algorytmy%20z%20wyk%C5%82ad%C3%B3w/Programowanie%20dynamiczne/%5BDynamiczne%5D%20Najd%C5%82u%C5%BCszy%20rosn%C4%85cy%20podci%C4%85g%20(niesp%C3%B3jny).ipynb
# https://cp-algorithms.com/sequences/longest_increasing_subsequence.html#alternative-way-of-restoring-the-subsequence


def binarySearch(A, value):
    #
    start = 0 
    end   = len(A) - 1

    while start <= end:
        middle = ( start + end ) // 2

        if value > A[middle]: start += 1
        else: end -= 1

    #end while 
    return start 
#end procedure binarySearch 


def LongestIncreasingSubsequence(A):
    #
    n = len(A)
    F = []

    for i in range(n):
        idx = binarySearch(F, A[i])

        if idx == len(F): F.append( A[i] )
        else: F[idx] = A[i] 

    #end 'for' loop 

    return len(F)
#end procedure LongestIncreasingSubsequence()

A = [3, 1, 5, 7, 2, 4, 9, 3, 17, 3] # 5
print( LongestIncreasingSubsequence(A) )

A = [ 3, 10, 2, 1, 20 ] # 3
print( LongestIncreasingSubsequence(A) )  # 3 10 20

A = [ 50, 3, 10, 7, 40, 80 ] # 4
print( LongestIncreasingSubsequence(A) )  # 3 7 40 80

A = [ 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 ] # 6
print( LongestIncreasingSubsequence(A) )  # 0 2 6 9 13 15