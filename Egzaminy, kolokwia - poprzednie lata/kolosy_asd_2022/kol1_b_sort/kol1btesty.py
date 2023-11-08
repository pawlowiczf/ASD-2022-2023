# kol1btesty.py
from testy import *
from kol1btest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy



def copyarg( arg ):
    return deepcopy(arg)


def printarg(T):
    out = ', '.join(T[:20])
    print("Wejcie:\t", limit(out))


def printhint( hint ):
    print("Prawidlowy wynik:\t", hint)


def printsol( sol ):
    print("Wynik algorytmu:\t", sol)


def check( T, hint, sol ):
    return sol == hint

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
        
    TESTS[0]["arg"] = [ ["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"] ]
    TESTS[0]["hint"]= 4
      
    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

