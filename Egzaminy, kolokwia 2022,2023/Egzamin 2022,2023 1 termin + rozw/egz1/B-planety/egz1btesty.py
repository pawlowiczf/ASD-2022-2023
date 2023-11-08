# egz1btesty.py
from testy import *
from egz1btest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(D, C, T, B):
    print("Odleglosci planet: ", limit(D))
    print("Ceny paliwa      : ", limit(C))
    print("Teleporty        : ", limit(T))
    print("Pojemnosc baku   : ", B)


def printhint( hint ):
    print("Prawidlowy wynik : ", hint)


def printsol( sol ):
    print("Wynik algorytmu  : ", limit(sol))


def check( D, C, T, B, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good

 
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    D=[0, 5, 10, 20]
    C=[2, 1,  3,  8]
    T=[(2,3), (3,7), (2,10), (3,10)]
    B=10
    hint=17

    newtest = {}
    newtest["arg"] = [D, C, T, B]
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

