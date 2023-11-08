"""
Dostajac na wejsciu string zlozony z liter a-z, zwroc 
najdluzszy jego fragment, ktory jest palindromem.
"""

def Palindrom(S):
    #
    n = len(S)
    F = [ [ 0 for _ in range(n) ] for _ in range(n) ]
    
    for k in range(n):
        F[k][k] = 1
    #

    for a in range(n - 1):
        if S[a] == S[a+1]:
            F[a][a+1] = 1 
    #

    best = -1
    length = 3
    
    while length < n:
        a = 0 
        while a + length < n:

            if S[a] == S[a+length] and F[a + 1][ a + length - 2 ]:
                F[a][a + length -1] = 1 
                best = max(best, length)
            #
            a += 1
        #end 'while' loop

        length += 1
    #end 'while' loop

    return best 
#end procedure Palindrom()
    

S = "cacabbbbbaccbccbccacbca"
print( Palindrom(S) )



"""
Inne rozwiazanie, niewykorzystujace DP:

def expand_from_mid(T, i, j):
    while i >= 0 and j < len(T):
        if T[i] != T[j]: 
            break
        i -= 1
        j += 1
    return j - i - 1, j - 1  


def get_longest_palindrome(S):
    if len(S) < 2: return S
    
    max_end = 0
    max_length = 1
    for i in range(1, len(S)):
        # Handle odd number of values case
        odd_length, odd_end = expand_from_mid(S, i, i)
        # Handle even number of values case
        even_length, even_end = expand_from_mid(S, i - 1, i)
        # Get the max length and update the global max if
        # found a longer subsequence than the previous longest
        if odd_length > even_length:
            if odd_length > max_length:
                max_length = odd_length
                max_end = odd_end
        else:
            if even_length > max_length:
                max_length = even_length
                max_end = even_end
    
    return S[max_end - max_length + 1 : max_end + 1]


"""