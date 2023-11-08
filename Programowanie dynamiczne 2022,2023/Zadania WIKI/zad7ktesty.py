import time 
from collections import deque

TEST_SPEC = [
# D (szerokosc), N (ilosc), H (wysokosc), M (max. woda), W (max. wartosc), LIMIT WODY, WYNIK
  (5, 4, 4, 50, 15, 32, 28),
  (5, 15, 5, 50, 50, 154, 347),
  (5, 25, 5, 50, 50, 264, 535),
  (10, 25, 5, 50, 50, 205, 500),
  (25, 50, 20, 70, 50, 939, 1092),
  (50, 50, 50, 100, 50, 1169, 1145),
  (100, 100, 50, 120, 50, 2619, 2152),
  (150, 250, 50, 50, 50, 3075, 5194),
  (100, 400, 50, 10, 50, 1213, 8284),
  (150, 650, 50, 5, 50, 894, 13214),
]

MY_seed    = 42
MY_a       = 134775813
MY_c       = 1
MY_modulus = 2**32

def MY_random():
   global MY_seed, MY_a, MY_c, MY_modulus
   MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
   return MY_seed

total = 0

def bfs(T, V, y, m, D, N, H, M, W):
    global total
    Q = deque()
    V[0][y] = MY_random()%(m//10+1)+1
    total += V[0][y]
    
    Q.append((1, y))
    col = 0 
    
    while Q and col < m:
        u = Q.popleft()
    
        if V[u[0]][u[1]] != 0:
            continue 
    
        r = MY_random()%(m//10+1)+1
        V[u[0]][u[1]] = r 
        col += r
        total += r
    
        if u[0]-1 >= 1 and T[u[0]-1][u[1]] != 0:
             Q.append((u[0]-1, u[1]))
        if u[0]+1 < H and T[u[0]+1][u[1]] != 0:
             Q.append((u[0]+1, u[1]))
        if u[1]-1 >= 0 and T[u[0]][u[1]-1] != 0:
             Q.append((u[0], u[1]-1))
        if u[1]+1 < N*D+1 and T[u[0]][u[1]+1] != 0:
             Q.append((u[0], u[1]+1))

def runtests( f, all_tests = True ):
    global total
    global TEST_SPEC
    zaliczone = 0 
    testy = 0
    ii = 0
    totaltime = 0
    if all_tests == False:
        TEST_SPEC = [TEST_SPEC[0], TEST_SPEC[1], TEST_SPEC[2]]
    for el in TEST_SPEC:
        D = el[0]
        N = el[1]
        H = el[2]
        M = el[3]
        W = el[4]

        total = 0
        DD = []
        ZZ = []
        
        T = [[MY_random()%(4) for _ in range(N*D+1)] for _ in range(H)]
        V = [[0 for _ in range(N*D+1)] for _ in range(H)]
        
        for i in range(N*D+1):
            T[0][i] = 0
            T[1][i] = 0
        
        for i in range(N):
            for e in range(H):
                T[e][i*D] = 0
        
        for i in range(N):
            r = MY_random()%(D-1)+1
            T[0][r+i*D] = 1
            T[1][r+i*D] = 1
            DD.append(r+i*D)
            ZZ.append(MY_random()%(W)+1)
            m = MY_random()%(M+1)+M//10
            bfs(T, V, r+i*D, m, D, N, H, M, W)
        
        
        
        start = time.time()
        sol = f(V, DD, ZZ, total//2)

        end = time.time()
        totaltime += (end-start)
        testy += 1 
        if sol == el[6]:
            print("TEST #", ii, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[6])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", ii, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[6])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        ii += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(totaltime))