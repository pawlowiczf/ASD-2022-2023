import time 
import sys 

sys.setrecursionlimit(2500)

TEST_SPEC = [
# N (długość tablicy), P (procent na zepsucie), dlugosc? 
#(True = zazwyczaj dodawaj/False = zazwyczaj usuwaj) hint (poprawna odpowiedź)
  (10, 50, True, 3),
  (10, 20, False, 3),
  (20, 40, False, 9),
  (50, 90, True, 44),
  (100, 30, True, 35),
  (200, 60, False, 107),
  (300, 20, False, 72),
  (400, 90, True, 344),
  (500, 70, False, 302),
  (600, 80, True, 457),
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
        s = ""
        for j in range(el[0]):
            s = s + chr(((MY_random()%26)+97))

        t = ""
        for i in range(el[0]):
            rand = MY_random()%100 
            if rand < el[1]:
                no = 80 
                if el[2] == False:
                    no = 240 
                ch = MY_random()%no
                if ch%2 == 0: 
                    t = t + s[i] + chr(((MY_random()%26)+97))
                    pass
                else:
                    if ch < 60:
                        t = t[:-1]
                    else:
                        t = t + chr(((MY_random()%26)+97))
            else:
                t += s[i]

        if ii == 0:
            s = "swidry"
            t = "kawiory"
        
        start = time.time()
        sol = f(s, t)
        end = time.time()
        total += (end-start)
        testy += 1 
        if sol == el[3]:
            print("TEST #", ii, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", ii, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        ii += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

