# Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku miesci sie dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajduja sie stacje benzynowe (na pozycjach bedacych liczbami naturalnymi; A
# jest na pozycji 0). Prosze podac algorytmy dla nastepujacych przypadków:

# (1) Wyznaczamy stacje na których tankujemy tak, zeby łaczna liczba tankowan była minimalna.

# (2) Wyznaczamy stacje tak, zeby koszt przejazdu był minimalny (w tym wypadku kazda stacja ma dodatkowo
# cene za litr paliwa). Na kazdej stacji mozemy tankowac dowolna ilosc paliwa.

# (3) j.w., ale jesli na stacji tankujemy, to musimy zatankowac do pełna.
# algorytm dynamiczny. F(i, fuel) - minimalny koszt dotarcia do stacji 'i', majac w zapasie 'fuel' litrow paliwa 
# F(0, 0) = 0
# F(0, fuel) = float('inf') (odrzucamy takie rozwiazania), gdzie fuel > 0 
# F(i, k) = min( F(i - 1, k + D[i - 1][i], min( F(i - 1, z) + (L - z) * C[i - 1] ), po 0 <= z <= L, D[i - 1][i] == L - k  )


# Podpunkt (1) --------------------------------------

def nextStation(S, left, right, value):
    #

    while left <= right:
        middle = ( left + right ) // 2
        
        if value < S[middle]:
            right = middle - 1 
        
        else:
            left = middle + 1 

    #
    return right 
#end procedure nextStation()


def Function1(S, L, d, fuel): # S - odleglosci do stacji benzynowych od indeksu 0, L - pojemnosc baku, d - odleglosc do celu, fuel - poczatkowa ilosc paliwa 
    #
    n = len(S)
    firstStation = nextStation(S, 0, n - 1, fuel)
    lastStation  = nextStation(S, 0, n - 1, d)

    if S[0] > fuel: return -1 
    if fuel >= d: return 0 

    count    = 0
    position = firstStation

    while position < lastStation: 
        #
        count += 1
        nextStop = nextStation(S, position + 1, lastStation, S[position] + L)

        if nextStop == position: return -1 # nie ma stacji, ktora mozna osiagnac z okreslonego punktu 'position'

        position = nextStop
    #

    return count if d - S[lastStation] <= L else -1
#end procedure Function1()

print(" ----------------- Podpunkt (1) -------------------- ")
L = 20
d = 105 
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 130, 135]
fuel = 1
print( Function1(S, L, d, fuel) ) # 7

L = 20
d = 138
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140]
fuel = 1
print( Function1(S, L, d, fuel) ) # -1

L = 20
d = 20
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140]
fuel = L
print( Function1(S, L, d, fuel) ) # 0

L = 20
d = 132
S = [0, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140]
fuel = 0
print( Function1(S, L, d, fuel) ) # 8

L = 20
d = 133
S = [0, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140]
fuel = 0
print( Function1(S, L, d, fuel) ) # -1 

print(" ------------------------------------------------- " )


# Podpunkt (2)
# Sprawdzamy stacje, na ktore mozemy sie udac. Jesli istnieje tansza stacja w naszym zasiegu (lub przy pelnym baku, wtedy tankujemy, tyle aby sie tam dostac),
# to idziemy tam. (wybieramy pierwsza, najtansza stacje w naszym zasiegu)
# Jesli nie istnieje tansza stacja, to tankujemy na maksa i idziemy na kolejna stacje i ponawiamy krok 1 

def firstStationIndex(S, C, L):
    #
    n = len(S)
    minIdx = 0

    for station in range(1, n):
        #
        if S[station] > L: break 
        if C[station] < C[minIdx]: minIdx = station 
    #

    return minIdx
#end procedure firstStationIndex()


def nextStationIndex(L, S, C, d, fuel, position):
    #
    minIndex = position 

    a = position + 1
    minIds = a

    while a < len(S) and S[a] - S[position] <= L:
        #
        if C[a] < C[position]: return a 
        if C[a] < C[minIdx]: minIdx = a 
    #
    return minIdx
#end procedure nextStationIndex()


def Function2(L, S, C, d, fuel): # L - pojemnosc baku, S - odleglosci do stacji od punktu poczatkowego, C - koszt 1 litra na stacji, d - dlugosc trasy, fuel - poczatkowa wartosc paliwa 
    #
    n = len(S)
    cost = 0 

    position = firstStationIndex(S, C, L)

    while position < lastStation:

