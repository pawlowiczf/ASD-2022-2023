'''
Opis algorytmu:
Algorytm wykorzystuje strukture kopca max, stad dodatkowe funkcje pomocnicze: heapify, buildheap.
Dzialanie algorytmu polega na zbudowaniu kopca z podanej tablicy z danymi, a nastepnie 
dodawanie do zmiennej sum_snow najwiekszych elementow tablicy tj. korzenia kopca T[0], dopoki
jest snieg (dopoki nie stopnial tj. S[0] - pom > 0 ). 
Korzystam z kopca max, gdyz nie ma potrzeby sortowac calej tablicy, bo snieg topnieje.

Tak przedstawiony algorytm dziala, gdyz to, czy zaczniemy brac snieg od wejsc, czy od elementu najwiekszego
nie ma znaczenia - suma zebranego sniegu bedzie taka sama, bo ten topnieje. Najlepiej opisac to na przykladzie:
S = [15,16,3,59,24,16]. Widac, ze najlepiej zaczac od prawej strony i wziac 16,24,59 itd ; suma sniegu to bedzie
16 + 23 + 57 = 96 itd..., ale te sama sume dostaniemy, gdy wezmiemy 59 + 23 + 14 = 96 , gdyz snieg stopnial 
w kazdym przypadku o 3. Widzimy wiec, ze nie ma znaczenia efektywny wybor sniegu z wejsc, czy branie go od wartosci najwiekszych w "posortowanej" tablicy.

Zlozonosc O(nlogn)
'''

from zad2testy import runtests

#
def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return ( i - 1 ) // 2
#

def heapify(A, i, n):
    #
    l = left(i)
    r = right(i)
    max_ind = i
    #
    if l < n and A[ l ] > A[ max_ind ]: max_ind = l
    if r < n and A[ r ] > A[ max_ind ]: max_ind = r 
    #
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)
    #end if 

#end def heapify() ^^^


def buildheap(A):
    n = len(A)
    #
    for i in range( parent( n - 1 ), -1, -1):
        heapify(A, i, n)
#end def buildheap() ^^^


def snow( S ):
    #
    n = len(S)
    index = n - 1
    sum_snow = 0
    pom = 0
    #
    buildheap(S)
    #
    while S[ 0 ] - pom > 0 and index >= 0:
        S[0], S[index] = S[index], S[0]
        sum_snow += S[ index ] - pom
        heapify(S, 0, index)
        pom += 1
        index -= 1
    #end while

    return sum_snow
#end def snow() ^^^

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )


