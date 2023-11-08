"""
Asystent znanego profesora otrzymal polecenie wyliczenia sumy pewnego ciagu liczb ( liczby moga byc
zarowne dodatnie, jak i ujemne). Aby zminimalizowac bledy zaokraglen asystent postanowil wykonywac powyzsze
dodawania w takiej kolejnosci, by najwiekszy co do wartosci bezwzglednej wynik tymczasowy ( wynik 
kazdej operacji dodawania ; wartosc koncowej sumy rowniez traktujemy jak wynik tymczasowy ) byl mozliwie
jak najmniejszy. Aby ulatwic sobie zadanie, asystent nie zmienia kolejnosci liczb w sumie, a jedynie wybiera kolejnosc dodawan.

Napisz funkcje, ktora zwraca najwieksza wartosc bezwzgledna wyniku tymczasowego.

Np. dla tablicy [1, -5, 2] funkcja powinna zwrocic wartosc 3, co odpowiada dodaniu -5 i 2, a nastepnie dodaniu 1 do wyniku.
"""


def opt_sum(A):
    n = len(A)
    INF = -float('inf')
    F = [[INF] * n for _ in range(n)]
    
    S = [0] * (n + 1)
    S[0] = A[0]
    for i in range(1, n):
        S[i] = A[i] + S[i - 1]
    
    def recur(i, j):
        if i == j:
            F[i][j] = 0  # Store 0 as we do not add anything
        elif j - i == 1: 
            F[i][j] = abs(A[i] + A[j])
        elif F[i][j] == INF:
            sum_ = abs(S[j] - S[i - 1])
            for k in range(i, j):
                F[i][j] = max(min(recur(i, k), recur(k + 1, j), sum_), F[i][j])
                
        return F[i][j]
    
    recur(0, n - 1)
    print(*F, sep='\n')
    return F[0][n - 1]


A = [1, -5, 2]

print(opt_sum(A))