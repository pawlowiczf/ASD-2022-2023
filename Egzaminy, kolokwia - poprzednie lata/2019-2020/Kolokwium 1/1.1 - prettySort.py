"""[2pkt.] Zadanie 1. Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
pretty_sort(T)
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową."""
def convert(n):
    A = [0] * 10
    temp = n
    while temp > 0:
        A[temp % 10] += 1
        temp //= 10
    single = 0
    many = 0
    for d in A:
        if d == 1:
            single += 1
        elif d > 1:
            many += 1
    return n, single, many


def countingsort(A, key):
    low, high = float("inf"), float("-inf")
    n = len(A)
    for el in A:
        low = min(low, el[key])
        high = max(high, el[key])

    cnt = [0] * (high - low + 1)

    for el in A:
        idx = el[key] - low
        cnt[idx] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]

    B = [0] * n
    for i in range(n - 1, -1, -1):
        idx = A[i][key] - low
        cnt[idx] -= 1
        B[cnt[idx]] = A[i]

    for i in range(n):
        A[i] = B[i]


def pretty_sort(A):
    n = len(A)
    for i in range(n):
        A[i] = convert(A[i])

    countingsort(A, 2)
    for i in range(n // 2):
        A[n - i - 1], A[i] = A[i], A[n - i - 1]
    countingsort(A, 1)

    for i in range(n):
        A[i] = A[i][0]

    for i in range(n // 2):
        A[n - i - 1], A[i] = A[i], A[n - i - 1]
