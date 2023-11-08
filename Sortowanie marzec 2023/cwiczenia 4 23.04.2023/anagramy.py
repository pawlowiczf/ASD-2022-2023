# Sprawdz, czy dwa slowa sa anagramami
# Jesli dlugosc znaku jest mala, k ( max. 25 znakow )
# Najlepiej zeby n = k


# 1 sposob:
# O(n+k)

# Tutaj mamy tablice z liczbami
def count(A,B,k): # k - ilosc roznych liter 
    n = len(A)
    letters = [0 for _ in range(k) ]
    #
    for i in range(n):
        letters[ A[i] ] += 1 
        letters[ B[i] ] -= 1 
    #
    for i in range(k):
        if letters[i] != 0: return False 
    #
    return True 
#end def ^^^

# last z - ascii 122 
# first A - ascii  65 

def anagram(A,B,k):
    Count = [ 0 for i in range( k ) ]
    #
    if len(A) != len(B): return False
    #
    for i in range( len(A) ):
        Count[ ord( A[i] ) - ord('a') ] += 1
        Count[ ord( B[i] ) - ord('a') ] -= 1
    #
    for i in range( k ):
        if Count[i] != 0: return False
    #
    return True
#end def ^^^



# 2 sposob:
# Jesli k > 25 ( k > n )

def count2(A,B,k): # k - ilosc roznych liter 
    n = len(A)
    letters = getEmptyTable(k)
    for i in range(n): #nie ma co tworzyc tablicy o dlugosci k, bo to jest k-liniowe. 
        letters[ A[i] ] = 0
        letters[ B[i] ] = 0
    #
    for i in range(n):
        letters[ A[i] ] += 1 
        letters[ B[i] ] -= 1 
    #
    for i in range(n):
        if letters[ A[i] ] != 0 or letters[ B[i] ] != 0: return False
    #
    return True 
#end def ^^^

# Pusta tablica ze smieciami:
def getEmptyTable(n):
    pass


A = "abba"
B = "baba"

print( anagram(A,B,26) )

print( ord('a') )
print( ord('A') )