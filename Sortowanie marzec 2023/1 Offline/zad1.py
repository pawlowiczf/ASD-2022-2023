'''
Funkcja pomocnicza palindrom(s, position) znajduje dlugosc palindromu zaczynajac od srodka (liczba znakow palindromu nieparzysta) 
i rozszerza swoj "promien", dopoki odpowiednie znaki sie zgadzaja (tj. s[position - pom] == s[position + pom] ). Jesli kolejne wyrazy sie 
nie beda zgadzac, przerywa dzialanie i zwraca dotychczasowa dlugosc. Dlugosc kazdego palindromu na pewno jest nieparzysta, gdyz w kazdej iteracji
petli while sprawdzamy 2 znaki, czyli lacznie 2*pom oraz dodajemy 1 znak, ktory jest srodkiem. Razem 2k+1.

Glowna funkcja ceasar( s ) przechodzi po znakach stringa (i, od indeksu 1, do len(s) - 1, aby funkcja palindrom nie wyrzucila bledu wyjscia 
poza zakres ) i przekazuje do funkcji palindrom(s, i) indeks i na ktorym obecnie znajduje sie petla for. Jesli zwrocona dlugosc
palindromu przez funkcje pomocnicza jest wieksza od dotyczczasowej (length) to ja aktualizuje. Przechodzac po kazdym znaku stringa
i wywolaniu dla niego funkcji pomocniczej, kazdy potencjalny najdluzszy palindrom Cesarzowej zostanie sprawdzony.

Kazdy wyraz 1 znakowy jest palindromem, dlatego zakladam, inicjucjac zmienna, ze length = 1 
Jesli string jest pusty, to length = 0

Zlozonosc O(n^2)

'''

from zad1testy import runtests


def palindrom(s, position):
    pom = 1
    length = len(s)
    #
    while position - pom >= 0 and position + pom < length:
        if not s[ position - pom ] == s[ position + pom ]: return 2*(pom-1) + 1
        pom = pom + 1
    #end while

    return 2*(pom-1) + 1

#end def ^^^


def ceasar( s ):
    #
    if s == "": return 0
    #
    length = 1
    N = len(s)
    #
    for i in range(1, N - 1):
        x = palindrom(s, i)
        if x > length: length = x
    #end for 

    return length

#end def ^^^


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )

