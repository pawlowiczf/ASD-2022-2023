# Sortowanie przez zliczanie
# Wiemy, ze  liczby naturalne w tablicy naleza do przedzialu [0, k-1], k > 0
# O(n + k) - jesli k zblizone do n, to mamy sortowanie liniowe O( n )

def counting_sort(A,B,k):
    C = [0] * k

    for i in range( len(A) ):
        C[ A[i] ] += 1
    # Tablica C zawiera ilosc wystapien danego elementu w tablicy A 

    for i in range(1, k ):
        C[i] = C[i] + C[i-1]
    # Tablica C zawiera teraz ilosc liczb poprzedzajacych i wraz z nimi

    for i in range( len(A) - 1, -1, -1 ): # przez to ze idziemy od konca mamy stabilnosc
        B[ C[ A[i] ] - 1 ] = A[i]
        C[ A[i] ] -= 1

#end def ^^^




# rozmiar tablicy B taki sam, jak rozmiar A
# rozmiar tablicy C w zaleznosci od przedzialu liczb [0,k]

T = [1,4,1,2,7,5,2]
B = [0]*7
counting_sort(T, B, 15)
print( B )



