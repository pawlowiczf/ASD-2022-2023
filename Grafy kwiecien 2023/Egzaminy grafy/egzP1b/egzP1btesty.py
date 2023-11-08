import time 

TEST_SPEC = [
# M (max. wierzchołek), N (potencjalnie losowych krawedzi), max (max. waga, min - 1), hint (poprawna odpowiedź)
  (10, 0.4, 9, 7),
  (50, 0.5, 40, 35),
  (250, 0.6, 40, 31),
  (500, 0.3, 150, 159),
  (750, 0.1, 1500, 501),
  (1000, 0.05, 15, 34),
  (1250, 0.01, 50, 62),
  (5000, 0.002, 100, 208),
  (15000, 0.001, 100, 134),
  (50000, 0.0001, 200, 242),
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
        s = 0 
        k = el[0]

        G = []

        for j in range(int(el[0]*el[0]*el[1])):
            a = int(MY_random()%el[0])
            b = int(MY_random()%el[0])
            w = int(MY_random()%el[2]) + 1
            if a != b:
                G.append((min(a, b), max(a, b), w))
        
        a1 = int(MY_random()%(el[0]*0.3))
        a2 = int(MY_random()%(el[0]*0.6))
        while a2 == a1:
            a2 = int(MY_random()%(el[0]*0.6))
        a3 = int(MY_random()%(el[0]*0.9))
        while a3 == a1 or a3 == a2:
            a3 = int(MY_random()%(el[0]*0.9))
        w1 = int(MY_random()%el[2]) + 1
        w2 = int(MY_random()%el[2]) + 1 
        w3 = int(MY_random()%el[2]) + 1 
        w4 = int(MY_random()%el[2]) + 1 

        G.append((min(s, a1), max(s, a1), w1))
        G.append((min(a1, a2), max(a1, a2), w2))
        G.append((min(a2, a3), max(a2, a3), w3))
        G.append((min(a3, k), max(a3, k), w4))
        
        if i == 0:
            G = [
                (0, 1, 9), (0, 2, 1),
                (1, 2, 2), (1, 3, 8),
                (1, 4, 3), (2, 4, 7),
                (2, 5, 1), (3, 4, 7),
                (4, 5, 6), (3, 6, 8),
                (4, 6, 1), (5, 6, 1)
            ]

            s = 0
            k = 6
        
        start = time.time()
        sol = f(G, s, k)
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

