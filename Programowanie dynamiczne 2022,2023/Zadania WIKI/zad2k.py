from zad2ktesty import runtests

# Wyjasnienie znajduje sie w folderze 'BIT ALGO'

def checkPalindrom( S ):
    #
    n = len(S)
    F = [ [ False for _ in range(n) ] for _ in range(n) ]

    for char in range(n):
        F[char][char] = True 
    #

    for char in range(n - 1):
        if S[char] == S[char + 1]:
            F[char][ char + 1 ] = True 
    #

    cords = (-1, -1)
    bestLength = -1

    for length in range( 3, n ):
        for a in range( n - length + 1 ):

            b = a + length - 1
            if S[a] == S[b] and F[a + 1][b - 1]:
                F[a][b] = True

                if b - a + 1 > bestLength:
                    bestLength = b - a + 1
                    cords = (a, b)

    #end 'for' loops 

    a, b = cords  
    return S[ a : b + 1 ] if cords != (-1, -1) else None
#end procedure checkPalindrom()


def palindrom( S ):
    #
    return checkPalindrom( S )
#end palindrom()

runtests ( palindrom )