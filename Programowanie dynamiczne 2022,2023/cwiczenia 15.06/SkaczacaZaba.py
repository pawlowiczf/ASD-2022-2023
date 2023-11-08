# Pewna zaba skacze po osi liczbowej. Ma sie dostac z zera do n − 1, skaczac
# wyłacznie w kierunku wiekszych liczb. Skok z liczby i do liczby j (j > i) kosztuje ja j − i jednostek energii, a
# jej energia nigdy nie moze spasc ponizej zera. Na poczatku zaba ma 0 jednostek energii, ale na szczescie na
# niektórych liczbach—takze na zerze—leza przekaski o okreslonej wartosci energetycznej (wartosc przekaki
# dodaje sie do aktualnej energii Zbigniewa). Prosze zaproponowac algorytm, który oblicza minimalna liczbe
# skoków potrzebna na dotarcie z 0 do n − 1 majac dana tablice A z wartosciami energetycznymi przekasek na
# kazdej z liczb.

# F(i, k) - minimalna liczba skokow, by dotrzec z pola 'i' do konca, majac na polu 'i' k energi 
# ( przed zjedzeniem przekaski na polu 'i' )

# F(n, k) = 0 dla k >= 0, 1 <= j <= n
# F(n, k) = float('inf') dla k < 0, 1 <= j <= n
# F(i, k) = min( F[j][ k - ( j - i ) + A[i] ] + 1 ), j <= i + k + A[i]


def JumpingFrog(T):
    #
    n = len(T)
    F = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]

    for energy in range(n):
        F[n - 1][energy] = 0
    #

    for x in reversed( range(n - 1) ):
        for energy in range(n):
            for y in range(x + 1, min(n, x + energy + T[x] + 1) ):

                if energy - ( y - x ) + T[x] >= 0:
                    F[x][energy] = min( F[y][ min( energy - (y - x) + T[x], n - 1) ] + 1 , F[x][energy] )

    #end 'for' loops 

    return F[0][0]
#end procedure JumpingFrog()


A = [2, 2, 1, 0, 0, 0]
print( JumpingFrog(A) ) # 3

A = [2, 3, 1, 1, 2, 0]
print( JumpingFrog(A) ) # 2

A = [5, 0, 0, 0]
print( JumpingFrog(A) ) # 1
