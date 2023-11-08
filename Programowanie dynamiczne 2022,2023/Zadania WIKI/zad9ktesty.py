import time 

TEST_SPEC = [
# N (długość tablicy), M (max. element), l1, l2, hint
  (0, 0, 0, 0, 5),
  (10, 15, 10, 15, 3),
  (50, 30, 50, 80, 12),
  (100, 15, 100, 20, 20),
  (200, 25, 300, 30, 25),
  (300, 50, 15, 500, 23),
  (400, 50, 80, 200, 10),
  (500, 70, 90, 230, 12),
  (600, 80, 260, 110, 9),
  (750, 50, 150, 150, 12),
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
    ii = 0
    for el in TEST_SPEC:
        T = []
        for j in range(el[0]):
            T.append(MY_random()%el[1])
        l1 = el[2]
        l2 = el[3]

        if ii == 0:
            T = [5, 6, 1, 3, 2, 4, 3, 5]
            l1 = 8
            l2 = 10
        
        start = time.time()
        sol = f(T, l1, l2)

        if len(sol) == 0:
            passed = False 
        else:
            suma1 = 0 
            suma2 = 0
            for i in range(el[2]):
                if i in sol:
                    suma1 += T[i]
                else:
                    suma2 += T[i]
                if i == sol[len(sol)-1]:
                    break
            passed = (max(suma1,suma2) <= max(l1,l2) and min(suma1,suma2) <= min(l1,l2) and sol[len(sol)-1]+1 == el[4])
        

        end = time.time()
        total += (end-start)
        testy += 1 
        if len(sol) == 0:
            print("TEST #", ii, " NIEZALICZONY!")
            print("Poprawny ostatni element: ", el[4]-1, "\nTwój ostatni element: BRAK")
            print("Twoja odpowiedź: ", sol)
            print("Czas trwania: %.2f sek.\n" %float(end-start))
        elif passed:
            print("TEST #", ii, " zaliczony")
            print("Poprawny ostatni element: ", el[4]-1, "\nTwój ostatni element: ", sol[len(sol)-1])
            print("Twoja odpowiedź: ", sol)
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", ii, " NIEZALICZONY!")
            print("Poprawny ostatni element: ", el[4]-1, "\nTwój ostatni element: ", sol[len(sol)-1])
            print("Twoja odpowiedź: ", sol)
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        ii += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

