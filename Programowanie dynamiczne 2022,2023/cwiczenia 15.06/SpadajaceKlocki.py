# Kazdy klocek to przedział postaci [a, b]. Dany jest ciag klocków [a1, b1],
# [a2, b2], . . ., [an, bn]. Klocki spadaja na os liczbowa w kolejnosci podanej w ciagu. Prosze zaproponowac
# algorytm, który oblicza ile klocków nalezy usunac z listy tak, zeby kazdy kolejny spadajacy klocek miescił
# sie w całosci w tam, który spadł tuz przed nim.

# Jest to problem podobny do ukladania blokow w wieze ( Box Stacking )
# U nas kazdy blok ma wysokosc 1, wiec szukamy najwyzszej wiezy.
# Wynik to 'liczba klockow - wysokosc najwyzszej wiezy'


def Klocki(T):
    #
    n = len(T)

    # F(i) - wysokosc najwyzszej wiezy, gdy klocek 'i' znajduje sie na samej gorze 
    F = [ 1 for _ in range(n) ]

    for boxOne in range(1, n):
        a, b = T[ boxOne ] 

        for boxTwo in range( boxOne ):
            y, x = T[ boxTwo ]

            if y <= a <= b <= x:

                F[boxOne] = max( F[boxOne], F[boxTwo] + 1 )

    #end 'for' loops 

    return n - max( F )
#end procedure Klocki()


T = [ [0, 5], [1, 4], [-3, 7], [2, 3], [2, 6], [4, 6], [2, 3] ]
print( Klocki(T) ) # 3

T = [ (0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20) ]
print( Klocki(T) ) # 6