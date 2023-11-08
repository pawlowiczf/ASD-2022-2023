# egz3btesty.py
from testy import *
from egz3btest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg( P ):
    print("n                : ", len(P))
    print("P                : ", limit(P));

def printhint( hint ):
    print("Przykladowy wynik: ", hint)


def printsol( sol ):
    print("Wynik algorytmu  : ", sol)


def check( P, hint, sol ):
    good = True

    
    try:
      i = sol[0]
      j = sol[1]
    except:
      print("Błąd! Nieprawidlowy wynik algorytmu.")
      return False

    print("i                : ", i )
    print("j                : ", j )
    print("P[i]             : ", P[i] )
    print("P[j]             : ", P[j] )

    A = min( P[i], P[j] )
    B = max( P[i], P[j] )

    
    if A[0] == B[0] or A[1] == B[1]:
        good = False
    elif A[1] < B[0]:
        good = False
    elif B[1] < A[1]:
        good = False
    

    if not good:
        print("Błąd! Nieprawidlowy wynik algorytmu.")

    return good

 
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    P =[ [1,3], [6,7], [2,6], [4,6], [1,8], [5,10] ]
    hint = (2,1)
    newtest = {}
    newtest["arg"] = [P]
    newtest["hint"] = hint
    TESTS.append(newtest)

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)
        
    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

