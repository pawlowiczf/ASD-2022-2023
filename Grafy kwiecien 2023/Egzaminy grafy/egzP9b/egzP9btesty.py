from math import inf
import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
ALLOWED_TIME = 0.5

global k_seed
k_seed = 0

TEST_SPEC = [
#    n,         len_T,      len_Q
    (0,         0,          0),
    (5,         10,         4),
    (10,        50,         10),
    (25,        7500,       2500),
    (40,        12000,      3000),
    (50,        15000,      4000),
    (60,        18000,      5000),
    (70,        21000,      6000),
    (80,        24000,      7000),
    (90,        27000,      8000),
]


def randint_seed(a, b):
  global k_seed
  output = randint(a, b)
  k_seed += 1
  seed(k_seed)
  return output


def gentest(n, len_T, len_Q):
    global k_seed
    T = None
    Q = None
    if n == 0:
        T = [
            [1, 0, 2], #0
            [2, 0], #1
            [1, 0]  #2
        ]
        Q = [
            [0],
            [],
            []
        ]
    else:
        T = [[] for _ in range(n)]
        Q = [[] for _ in range(n)]
        vec = 0
        next_vec = None

        for _ in range(len_T):
            next_vec = randint_seed(0, n - 1)
            T[vec].append(next_vec)
            vec = next_vec
        T[next_vec].append(0)
        vec = 0

        for _ in range(len_Q):
            next_vec = randint_seed(0, n - 1)
            T[vec].append(next_vec)
            Q[vec].append(next_vec)
            vec = next_vec
        T[next_vec].append(0)
        Q[next_vec].append(0)

    for i in range(n):
        T[i].append((i + 1) % n)

    for el in T:
        shuffle(el)

    for el in Q:
        shuffle(el)
     
    return [T, Q]


RERAISE = True

def print_err(*a):
    print(*a, file = sys.stderr)
 
# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

def limit(L, lim = 80):
    x = str(L)
    if len(x) < lim:
        return x
    else:
        return x[:lim]+"[za dlugie]..."

class TimeOut(Exception):
  def __init__(self):
    pass

def internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ACC_TIME ):
  seed(0)
  passed, timeout, answer, exception = 0, 0, 0, 0

  print("Generowanie testów. Proszę czekać...")
  print("(!) To może zająć kilka sekund...")

  if all_tests == False:
    TESTS = generate_tests(3)
  else:
    TESTS = generate_tests(100)

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
    T = deepcopy(arg[0])
    Q = deepcopy(arg[1])
    try:
      time_s = time.time()
      sol = f(*arg)
      time_e = time.time()
      res = check(T, Q, sol)
      printhint(sol)
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
        print("TEST NIEZALICZONY!!!")
        status_line += ' W'
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

def printhint(sol):
    print(f"Otrzymany wynik: {limit(sol)}")

def printsol(sol):
  pass

def check(T, Q, sol):
    n = len(T)
    k = 1
    for el in T:
        k += len(el)
    for el in Q:
        k -= len(el)

    if len(sol) != k:
        return False

    A = [[0 for _ in range(n)] for _ in range(n)]
    A[0][0] += 1
    for i in range(n):
        for el in T[i]:
            A[i][el] += 1
        if len(Q[i]):
            for el in Q[i]:
                A[i][el] -= 1

    vec = 0
    for i in range(len(sol)):
        A[vec][sol[i % len(sol)]] -= 1
        vec = sol[i]

    for row in A:
        for el in row:
            if el != 0:
                return False

    return True
    
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg = gentest(*spec)
        newtest["arg"] = arg
        TESTS.append(newtest)
              
    return TESTS
 
def runtests(f, all_tests = 3):
    internal_runtests( copyarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

