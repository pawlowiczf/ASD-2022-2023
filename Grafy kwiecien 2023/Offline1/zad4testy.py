# zad4testy.py
from testy import *
from zad4test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg( G, s , t):
    print("G : ", limit(G))
    print("s : ", s)
    print("t : ", t)


def printhint( hint ):
    print("Mozliwe wyniki  : ", limit(hint) )


def printsol( sol ):
    print("Otrzymany wynik : ", limit(sol) )


def check( G, s, t, hint, sol ):
    if sol == None:
      print("*")
      if len(hint) == 0: return True
      return False
    sol = (min(sol), max(sol))
    if sol in hint: return True    
    return False
    
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


 
def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

