# kol1testy.py
from testy import *
from kol1test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(T, k, p):
    print("T = ", limit(T))
    print("k = ", k)
    print("p = ", p)


def printhint( hint ):
    print("Prawidlowy wynik:\t", hint)


def printsol( sol ):
    print("Wynik algorytmu:\t", limit(sol))


def check( T, k, p, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good

 
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = [{}]
    TESTS[0]["arg"] = [[7,9,1,5,8,6,2,12], 4, 5]
    TESTS[0]["hint"]= 17

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

