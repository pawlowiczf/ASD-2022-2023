import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
ALLOWED_TIME = 7


global k_seed
k_seed = 0

TEST_SPEC = [
    #n (wierzcholki), m (krawędzie), hint (wynik)
    (0,               0,             19),
    (1,               0,             0),  
    (10,              20,            19),  
    (60,              100,           514),
    (115,             400,           11660),
    (400,             1000,          78939),
    (5000,            14000,         15383761),
    (10000,           30000,         67886077),
    (20000,           50000,         190489187),
    (20000,           60000,         276803259)
]

def randint_seed(a, b):
  global k_seed
  output = randint(a, b)
  k_seed += 1
  seed(k_seed)
  return output

def gentest(n, m, hint):
    G = [[] for _ in range(n)]
    if n == 0:
      G = [
      [(1, 15), (2, 5),  (3, 10)],
      [(0, 15), (2, 8),  (4, 5),  (5, 12)],
      [(0, 5),  (1, 8),  (3, 5),  (4, 6)],
      [(0, 10), (2, 5),  (4, 2),  (5, 11)],
      [(1, 5),  (2, 6),  (3, 2),  (5, 2)],
      [(1, 12), (4, 2),  (3, 11)]]

    elif n == 1:
      G = [
      [(3, 12), (2, 8)],
      [(3, 4), (6, 5)],
      [(4, 9), (0, 8)],
      [(0, 12), (1, 4)],
      [(5, 8), (2, 9)],
      [(6, 2), (4, 8)],
      [(1, 5), (5, 2)]]

    else:
      r = randint_seed(1, n)
      T = []
      for i in range(n - 1):
        T.append(((i + r) % n, (i + r + 1) % n))
      for i in range(m - n + 1):
        a, b = 0, 0
        while a >= b:
          a = randint_seed(0, n - 1)
          b = randint_seed(0, n - 1)
        T.append((a, b))
      T = list(dict.fromkeys(T))

      G = [[] for _ in range(n)]
      for i in T:
        k = randint_seed(1, n)
        G[i[0]].append((i[1], k))
        G[i[1]].append((i[0], k))
       
    return G, hint

RERAISE = True

def print_err(*a):
    print(*a, file = sys.stderr)
 
# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

def limit(L, lim = 120):
    x = str(L)
    if len(x) < lim:
        return x
    else:
        return x[:lim]+"[za dlugie]..."

class TimeOut(Exception):
  def __init__(self):
    pass
       
def timeout_handler(signum, frame):
   raise TimeOut()

def internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ACC_TIME ):
  seed(0)
  passed, timeout, answer, exception = 0, 0, 0, 0

  print("Generowanie testów. Proszę czekać...")
  print("(!) To może zająć kilka sekund...")

  if all_tests == False:
    TESTS = generate_tests(3)
  else:
    TESTS = generate_tests(10)

  # A - Accepted
  # T - Timeout
  # W - Wrong Answer
  # E - Exception when solving
  # O - Terminated by operator
  status_line = ''

  total  = len(TESTS)
  total_time = 0
  for i,d in enumerate(TESTS):
    print("-----------------")
    print("Test", i )
    arg  = copyarg(d["arg"])
    hint = deepcopy(d["hint"])
    printhint( hint )
    try:
      time_s = time.time()
      sol    = f(arg)
      time_e = time.time()
      
      printsol( sol )
      res = check(hint, sol)
      if ACC_TIME > 0 and float(time_e-time_s) > ACC_TIME:
        timeout += 1
        status_line += ' T'
        print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
      elif res:
        passed += 1
        status_line += ' A'
        print("Test zaliczony!")
      else:
        answer += 1
        status_line += ' W'
        print("TEST NIEZALICZONY!!!")
      print("Orientacyjny czas: %.2f sek." % float(time_e-time_s))
        
      total_time += float(time_e-time_s)
    except TimeOut:
      timeout += 1
      status_line += ' T'
      print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
    except KeyboardInterrupt:
      exception += 1
      status_line += ' O'
      print("Obliczenia przerwane przez operatora")
    except Exception as e:
      exception += 1
      status_line += ' E'
      print("WYJATEK:", e)
      if RERAISE: raise e
    
  print("-----------------")
  print("Liczba zaliczonych testów: %d/%d" % (passed,total))
  print("Liczba testów z przekroczonym czasem: %d/%d" % (timeout,total))
  print("Liczba testów z błędnym wynikiem: %d/%d" % (answer,total))
  print("Liczba testów zakończonych wyjątkiem: %d/%d" % (exception,total))
  print("Orientacyjny łączny czas : %.2f sek." % total_time)
  print("Status testów:%s" % status_line)


def copyarg(arg):
    return deepcopy(arg)

def printhint(hint):
    print("Oczekiwany wynik: ", round(hint, 4))

def printsol(sol):
    print("Otrzymany wynik : ", round(sol, 4))

def check(hint, sol):
    return abs(hint - sol) < 0.01
    
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)
              
    return TESTS
 
def runtests(f, all_tests = 3):
    internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

