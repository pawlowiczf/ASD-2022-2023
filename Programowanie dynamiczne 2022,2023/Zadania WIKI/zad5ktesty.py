import time 

TEST_SPEC = [
# N (długość tablicy), hint (poprawna odpowiedź)
  (0, 22),
  (10, 161),
  (10, 108),
  (20, 276),
  (50, 666),
  (100, 1211),
  (200, 2539),
  (400, 5433),
  (600, 8336),
  (800, 10272),
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
            T.append(MY_random()%50+1)

        if i == 0:
            T = [8, 15, 3, 7]
        
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

