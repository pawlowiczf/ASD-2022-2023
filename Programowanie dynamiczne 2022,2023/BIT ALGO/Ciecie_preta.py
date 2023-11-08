"""
Firma kupuje dlugie stalowe prety i tnie je na kawalki, ktore sprzedaje.
Kawalki maja dlugosc w metrach wyrazona zawsze liczba naturalna.
Dla kawalka dlugosci n metrow znane sa ceny kawalkosc dlugosci 1, 2, ..., n metrow.
Firma chce znac maksymalny zysk, ktory moze uzyskac z pociecia i sprzedania preta dlugosci n.

F(n) - maksymalny zysk ze sprzedazy preta dlugosci n 
P[i] - koszt sprzedazy preta dlugosci i 

F(k) = max{ P[1] + F(k-1), P[2] + F(k-2), ... , P[k-1] + F(1) }
F(k) = max( P[i] + F(k - i) for k - i >= 0 )
F(0) = 0 

"""

def cuttingRodRek(P, n):
    #
    F = [ -float('inf') for _ in range(n + 1) ]
    F[0] = 0
    
    def rek(P, F, n):
        #
        if n == 0: return 0 
        if F[n] != -float('inf'): return F[n] 

        for k in range(1, n + 1):
            F[n] = max( F[n], P[k] + rek(P, F, n - k) )
        #
        return F[n]
    #end def 
    
    rek(P, F, n)
    return F[n] 
#end procedure cuttingRodRek()
        


def cuttingRod(P, n): # n - dlugosc preta 
    #
    F = [ -float('inf') for _ in range(n + 1) ]
    F[0] = 0

    for k in range(1, n+1):
        for i in range(k+1):
            F[k] = max( F[k], F[k-i] + P[i] )
    #end 'for' loops 

    return F[n]
#end procedure cuttingRod()

P = [0, 1, 3, 6, 5, 3] 
n = 5
print( cuttingRod(P, n) )
print( cuttingRodRek(P, n) )