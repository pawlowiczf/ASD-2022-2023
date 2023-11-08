from math import inf
import sys
from copy import deepcopy
import time
from random import random, randint, seed, shuffle
ALLOWED_TIME = 10

global k_seed
k_seed = 0


class Node:
  def __init__(self, val, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = val
    self.x = None
  
  def __add__(self, other):
    return Node(self.key + other.val, None)

  def __mul__(self, other):
    return NotImplemented

  def __rmul__(self, other):
    return Node(self.key * other, None)

  def __eq__(self, other):
    if type(self) == Node and type(other) == Node:
      return self.key == other.val
    else:
      return False


TEST_SPEC = [
#    n,   m,      r,    p,    hint
    (0,   0,      0,    0,    6),
    (10,  40,     10,   4,    14),
    (15,  100,    20,   13,   39),
    (20,  100,    20,   8,    48),
    (50,  1000,   70,   12,   100),
    (75,  3000,   100,  60,   411),
    (100, 4000,   150,  30,   363),
    (150, 6000,   300,  120,  2071),
    (200, 15000,  500,  90,   2237),
    (300, 100000, 4000, 170,  12197)
]


def randint_seed(a, b):
  global k_seed
  output = randint(a, b)
  k_seed += 1
  seed(k_seed)
  return output


def gentest(n, m, r, p, hint):
    global k_seed
    G = None
    P = None
    if n == 0:
      G = [
        [(1, 3), (2, 3)],
        [(0, 3), (4, 4)],
        [(0, 3), (3, 1), (4, 4)],
        [(2, 1), (4, 2)],
        [(1, 4), (2, 4), (3, 2)]
      ]
      P = [0, 3, 4]
    else:
      K = [[inf for _ in range(n)] for _ in range(n)]
      for _ in range(m):
        x = randint_seed(0, n - 1)
        y = randint_seed(0, n - 1)
        v = randint_seed(1, r)
        K[x][y] = v
        K[y][x] = v

      G = [[] for _ in range(n)]
      for i in range(n):
        for j in range(n):
          if K[i][j] != inf:
            G[i].append((j, K[i][j]))

      P = [randint_seed(0, n - 1) for _ in range(p)]
      P = list(dict.fromkeys(P))

    return [G, P], hint


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
    hint = deepcopy(d["hint"])
    printhint( hint )
    try:
      time_s = time.time()
      sol    = f(*arg)
      printsol(sol)
      time_e = time.time()
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
    print("Oczekiwany wynik: ", hint)

def printsol(sol):
    print("Otrzymany wynik:  ", sol)

def check(hint, sol):
    return hint == sol
    
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

