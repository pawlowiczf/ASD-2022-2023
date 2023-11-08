"""[2pkt.] Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową."""
from quicksort import quickselect

""" Algorytm na początek za pomocą funkcji select wyszukuje obecne indeksy elementów,
które w posortowanej tablicy znajdowały by się na indeksach p i q, następnie wykonuje 
dwa przejścia quicksorta by między p i q trafiły wszystkie potrzebne elementy i wykonujemy już
pełnego quicksorta na tym właśnie przedziale """


def section(T, p, q):
    n = len(T)
    curr_p = quickselect(T, 0, n - 1, p)
    curr_q = quickselect(T, 0, n - 1, q)
    return T[p:q+1]


T = [10, 15, 34, 80, 97, 15, 24, 34, 11, 8, 2, 3]
print(section(T, 5, 8))
