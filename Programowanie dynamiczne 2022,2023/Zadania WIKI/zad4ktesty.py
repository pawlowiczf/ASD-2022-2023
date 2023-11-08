import time 
import sys 

sys.setrecursionlimit(2500)

TEST_SPEC = [
# N (długość tablicy), hint (poprawna odpowiedź)
  (0, 9),
  (10, 79),
  (10, 73),
  (20, 191),
  (50, 482),
  (100, 936),
  (200, 1829),
  (400, 3685),
  (600, 5480),
  (800, 7300),
]

MY_seed    = 42
MY_a       = 134775813
MY_c       = 1
MY_modulus = 2**32

def MY_random():
   global MY_seed, MY_a, MY_c, MY_modulus
   MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
   return MY_seed

def runtests( f ):
    total = 0 
    zaliczone = 0 
    testy = 0
    i = 0
    for el in TEST_SPEC:
        T = []
        for j in range(el[0]):
            x = []
            for k in range(el[0]):
                x.append(MY_random()%20)
            T.append(x)

        if i == 0:
            T = [
                [0, 5, 4, 3],
                [2, 1, 3, 2],
                [8, 2, 5, 1],
                [4, 3, 2, 0]
            ]

        
        T[0][0] = 0 
        T[el[0]-1][el[0]-1] = 0
        
        start = time.time()
        sol = f(T)
        end = time.time()
        total += (end-start)
        testy += 1 
        if sol == el[1]:
            print("TEST #", i, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[1])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", i, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[1])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        i += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

