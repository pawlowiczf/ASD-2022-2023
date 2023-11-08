import time 

TEST_SPEC = [
# N (długość tablicy), k (malarzy), M (max. liczba), hint (poprawna odpowiedź)
  (0, 0, 0, 35),
  (0, 0, 0, 60),
  (10, 3, 100, 179),
  (50, 5, 100, 470),
  (100, 15, 200, 672),
  (100, 25, 1000, 2390),
  (100, 100, 1000, 998),
  (200, 15, 100, 696),
  (400, 3, 1000, 70416),
  (4000, 1, 5, 12072),

]

MY_seed    = 42
MY_a       = 134775813
MY_c       = 1
MY_modulus = 2**32

def MY_random():
   global MY_seed, MY_a, MY_c, MY_modulus
   MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
   return MY_seed

def runtests( f, all_tests=True ):
    global TEST_SPEC
    if all_tests == False:
        TEST_SPEC = [TEST_SPEC[0], TEST_SPEC[1]]
    total = 0 
    zaliczone = 0 
    testy = 0
    i = 0
    for el in TEST_SPEC:
        T = []
        k = el[1]
        for j in range(el[0]):
            T.append(MY_random()%el[2]+1)
        if i == 0:
            T = [5,10,30,20,15]
            k = 3
        elif i == 1:
            T = [10,20,30,40]
            k = 2
        start = time.time()
        sol = f(T, k)
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

