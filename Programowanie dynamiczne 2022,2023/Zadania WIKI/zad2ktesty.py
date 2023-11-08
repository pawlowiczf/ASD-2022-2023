import time 

TEST_SPEC = [
# N (długość tablicy), k (max. litera), hint (poprawna odpowiedź)
  (10, 2, "abaaaba"),
  (10, 3, "acca"),
  (25, 3, "cacccac"),
  (50, 3, "babaccabab"),
  (250, 4, "ddcaaccaacdd"),
  (500, 4, "aabcabacbaa"),
  (500, 8, "ccggcc"),
  (1000, 12, "jbibj"),
  (1000, 24, "rfcfr"),
  (1000, 3, "bacabbbbcbbbbacab"),
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
            s = s + chr(97+(MY_random()%317)%el[1])
        
        start = time.time()
        sol = f(s)
        end = time.time()
        total += (end-start)
        testy += 1 
        if sol == el[2] or (len(sol) == len(el[2]) and el[2] == el[2][::-1]):
            print("TEST #", i, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPrzykładowa odpowiedz: ", el[2], "\nPoprawna długość: ", len(el[2]))
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", i, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPrzykładowa odpowiedz: ", el[2], "\nPoprawna długość: ", len(el[2]))
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        i += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

