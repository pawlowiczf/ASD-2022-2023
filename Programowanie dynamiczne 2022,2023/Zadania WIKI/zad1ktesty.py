import time 

TEST_SPEC = [
# N (długość tablicy), hint (poprawna odpowiedź)
  (0, 6),
  (0, -1),
  (10, 4),
  (20, 3),
  (50, 4),
  (100, 15),
  (500, 22),
  (750, 36),
  (1000, 50),
  (1250, 32),
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
        s = ""
        for j in range(el[0]):
            s = s + str((MY_random()%317)%2)

        if i == 0:
            s = "11000010001"
        if i == 1:
            s = "111111"
        
        start = time.time()
        sol = f(s)
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

