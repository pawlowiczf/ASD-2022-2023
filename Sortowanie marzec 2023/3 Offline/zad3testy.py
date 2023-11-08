# zad3testy.py
from testy import *
from zad3test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(T):
    if len(T) > 100:
        T = T[:100]
    out = ', '.join([w for w in T])
    print("Wejciowe napisy:\t", limit(out))


def printhint( hint ):
    print("Prawidlowy wynik:\t", hint)


def printsol( sol ):
    print("Wynik algorytmu:\t", limit(sol))


def check( T, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good

 
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
        
    TESTS[0]["arg"] = [["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]]
    TESTS[0]["hint"]= 3

    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

