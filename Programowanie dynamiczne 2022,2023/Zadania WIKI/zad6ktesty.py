import time 

TEST_SPEC = [
  # S (ciąg znaków S), hint (poprawna odpowiedź)
  ("27", 1),
  ("123", 3),
  ("18758", 2),
  ("12519", 6),
  ("1111019", 6),
  ("472031421512", 12),
  ("512300412351165151", 0),
  ("619873241351034132207161", 32),
  ("21311023232031235112045151", 144),
  ("61723430313251123513241611231", 0)
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
        s = el[0]
        
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

