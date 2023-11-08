# Dany jest ciag przedziałów postaci [ai, bi]. Dwa przedziały mozna
# skleic jesli maja dokładnie jeden punkt wspólny. Prosze wskazac algorytmy dla nastepujacych problemów:

# 1. Problem stwierdzenia, czy da sie uzyskac przedział [a, b] przez sklejanie odcinków.
# Wierzcholki to poczatki i konce: a, b. Krawedz istnieje miedzy a i b, jesli istnieje przedzial [a, b].
# Jesli istnieje sciezka miedzy [a,b] to przedzial da sie skleic 


# 2. Zadanie jak wyzej, ale kazdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
# To samo, co wyzej robimy, ale puszczamy Dijkstre z a.


# 3. Problem stwierdzenia jaki najdłuzszy odcinek mozna uzyskac sklejajac najwyzej k odcinków.
# F(l, x) - dlugosc najdluzszego przedzialu zlozonego z 'l' odcinkow, zaczynajacego sie w 'x' 
# F(0, _) = 0
# F(l, x) = 0, if nie ma odcinka, ktory zaczyna sie 'x' em 
# F(l, x) = max( F(l - 1, b) + ( b - x ) ) ), dla przedzialow [x:b] w zbiorze wszystkich przedzialow 
# Wynik to max( F(k, x) ), gdzie x to dowolny poczatek przedzialu w zbiorze wszystkich przedzialow


def LongestSegment( T, k, maxNumber):
    #
    n = len(T)
    F = [ [ 0 for _ in range(k + 1) ] for _ in range( maxNumber + 1 ) ]

    for (a, b) in T:
        F[a][1] = b - a 
    #

    for number in range(2, k + 1):
        for (a, b) in T:
            F[a][number] = max( F[a][number], F[b][number - 1] + ( b - a )  )

    #end 'for' loops 

    maxLength = -1 
    for a in range(n):
        for number in range(k + 1):
            maxLength = max( maxLength, F[a][number] )
    #

    return maxLength
#end procedure LongestSegment()
    

T = [ (0, 1), (1, 3), (2, 3), (3, 4), (5, 6), (6, 8), (8, 9) ]
print( LongestSegment(T, 3, 10) ) # 4

T = [ (0, 1), (1, 3), (2, 3), (3, 4), (5, 6), (6, 8), (8, 9), (1, 7) ]
print( LongestSegment(T, 3, 10) ) # 7