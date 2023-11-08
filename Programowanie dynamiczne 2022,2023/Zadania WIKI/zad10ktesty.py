import time 
import sys 

sys.setrecursionlimit(2500)

TEST_SPEC = [
# M (liczba), hint (poprawna odpowiedź)
  (6, 3),
  (100, 1),
  (145, 2),
  (248, 3),
  (542, 3),
  (319, 4),
  (786, 3),
  (791, 4),
  (1372, 4),
  (2168, 3),
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
        start = time.time()
        sol = f(el[0])
        end = time.time()
        total += (end-start)
        testy += 1 
        suma = 0 
        for ell in sol:
            suma += ell*ell
        if suma == el[0] and len(sol) == el[1]:
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

