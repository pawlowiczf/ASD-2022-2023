"""
Zab Zbigniew skacze po osi liczbowej. Ma sie dostac z zera do n-1, skaczac wylacznie w kierunku wiekszych liczb.
Skok z liczby i do liczby j (j > i ) kosztuje Zbigniewa j - i jednostek energi, a jego 
energia nigdy nie moze spasc ponizej zera. Na poczatku Zbigniew ma 0 jednostek energi, ale na szczescie na niektorych liczbach
- takze na zerze - leza przekaski o okreslonej wartosci energetycznej ( wartosc przekaski dodaje sie do aktualnej energi Zbigniewa ).
Funkcja powinna zwrocic minimalna liczbe skokow, potrzebna, zeby Zbigniew dotarl z zera do n-1
lub -1 jesli jest to niemozliwe.

Funkcja F(i, y) - minimalna liczba skokow potrzebna by dotrzec do liczby 'i' i miec w zapasie 'y' jednostek energi.


"""

def Jump(T):
    #
    n = len(T)
    F = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]


    def rek(i, f):
        #
        if i == n - 1: return 0
        f = min( f + T[i], n - 1 )

        if F[i][f] == float('inf'):
            for j in range(1, f + 1):
                if i + j < n:
                    F[i][f] = min( F[i][f], rek(i + j, min( f - j, n - 1 ) ) + 1 )
        #

        return F[i][f]
    #end def rek()

    return rek( 0, 0 )

#end procedure Jump()


A = [5, 0, 0, 0]
print(Jump(A))

A = [2, 2, 1, 0, 0, 0]
print(Jump(A))

A = [2, 3, 1, 1, 2, 0]
print(Jump(A))