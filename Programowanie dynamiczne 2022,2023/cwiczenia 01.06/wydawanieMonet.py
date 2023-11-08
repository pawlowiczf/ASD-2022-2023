# Mamy dana tablice z nominałami monet stosowanych w pewnym dziwnym
# kraju, oraz kwote T. Prosze podac algorytm, który oblicza minimalna ilosc monet potrzebna do wydania
# kwoty T (algorytm zachłanny, wydajacy najpierw najwieksza monete, nie działa: dla monet 1, 5, 8 wyda
# kwote 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).

"""
F(x) - najmniejsza ilosc monet potrzebna do wydania x (zloty)
F(x) = min( F(x - m ) + 1 ), gdzie m to dowolny nominal 

F(0) = 0 
F(t) = inf, dla t < 0 

"""


def money(T, M): # T - kwota, M - nominaly 
    #
    n = T + 1
    F = [ float('inf') for _ in range(n) ]
    F[0] = 0

    for x in range(1, n):
        for m in M:
            if x - m >= 0: 
                F[x] = min( F[x], F[ x - m ] + 1 )
    #end 'for' loops

    return F[T]
#end procedure money()


T = 15
M = [ 1, 5, 8 ]
print( money(T, M) )


T = 2
M = [2, 5]
print( money(T, M) )

T = 19
M = [ 2, 5 ]
print( money(T, M) )

T = 13
M = [ 2, 5 ]
print( money(T, M) )