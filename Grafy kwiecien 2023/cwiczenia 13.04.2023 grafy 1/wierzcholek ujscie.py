"""
Mówimy, że wierzchołek t w grafie skierowanym jest ujściem, jeśli:
- z każdego innego wierzchołka v istnieje krawędź z v do t,
- nie istnieje żadna krawędź wychodząca z t.
Podać algorytm znajdujący ujście (jeśli istnieje) przy macierzowej reprezentacji grafu.

"""

# Rozwiazanie kwadratowe: petle for 

"""
Jedziemy przez macierz, mamy wspolrzedne i, j, zaczynamy od lewego gornego rogu. Idziemy w prawo dopoki
sa zera. Jesli doszlismy do 1, to wtedy idziemy w dol i sprwadzamy, czy mozemy znowu isc w prawo ( patrzymy 
czy sa zera ). Czyli schodzimy w dol dopoki nie ma jedynki po prawej stronie. JEsli jest to idziemy w prawo. Postepujem
tak dopoki nie dojdziemy do prawej sciany. Jak doszlismy do sciany sprawdzamy czy dany wiersz nie jest
tym czego szukamy. Sprawdzamy ten wiersz i kolumne (jesli doszlismy od scainy w 5 indeksie, to sprawdzamy
piaty wiersz i piate kolumne). Jesli pasuje to znalezlizmy, jesli nie, to znaczy
ze nie istnieje. Czy i dlaczego mozemy byc pewni, ze go nie przegapimy? 
Jest tak, bo jesi idizemy w dol to ejst tylko jedna dziura, ktora przepusci nas w prawo do sciany,
jesli takiej nie znajdziemy, to nie ma takiego ujscia. 
"""

