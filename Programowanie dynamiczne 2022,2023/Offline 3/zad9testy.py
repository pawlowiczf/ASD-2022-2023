# zad9testy.py
from testy import *
from zad9test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(O, C, T, L):
    print("Pozycje parkingow:\t", limit(O))
    print("Ceny postoju:\t\t", limit(C))
    print("Limit kilometrow bez postoju:\t", T)
    print("Odleglosc z A do B:\t", L)


def printhint( hint ):
    print("Prawidlowy wynik:\t", hint)


def printsol( sol ):
    print("Wynik algorytmu:\t", limit(sol))


def check( O, C, T, L, hint, sol ):
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
        
    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

