import time 

TEST_SPEC = [
# N (długość tablicy), m (min. liczba), M (max. liczba), hint (poprawna odpowiedź)
  (0, 0, 0, 1),
  (0, 0, 0, 3),
  (0, 0, 0, 13),
  (5, 20, 100, 91),
  (7, 200, 1000, 881),
  (9, 500, 2500, 1867),
  (13, 1000, 5000, 2606),
  (15, 2000, 10000, 1344),
  (25, 2000, 5000, 0),
  (17, 200, 15000, 14401)
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
            T.append(MY_random()%el[1]+el[2])
        if i == 0:
            T = [1, 6, 5, 11]
        if i == 1:
            T = [1, 4]
        if i == 2:
            T = [20, 19, 18, 20, 16]
        start = time.time()
        sol = f(T)
        end = time.time()
        total += (end-start)
        testy += 1 
        if sol == el[3]:
            print("TEST #", i, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", i, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        i += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

