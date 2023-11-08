import time 

TEST_SPEC = [
# N (długość tablicy), w (max. liczba), k (k-pretty liczba), hint (poprawna odpowiedź)
  (0, 0, 4, 7),
  (10, 50, 3, 17),
  (10, 50, 5, 21),
  (20, 100, 20, 2),
  (500, 100, 1, 24402),
  (1000, 1000, 100, 205),
  (10000, 5000, 20, 220794),
  (15000, 5000, 30, 155893),
  (20000, 5000, 40, 117126),
  (25000, 15000, 100, 70722),
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

        if i != 0:
            for j in range(el[0]):
                T.append(MY_random()%el[1])
        else:
            T = [1, 2, 3, 4, 6, 15, 8, 7] 

        
        start = time.time()
        sol = f(T, el[2])
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

