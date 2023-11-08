# egz3atesty.py
from testy import *
from egz3atest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg( G, s, t ):
    print("Liczba zamkow     : ", len(G))
    print("Macierz sasiedztwa: ");
    for i in range(min(len(G),10)):
        print( limit(G[i]) )
    if len(G) >= 10: print("...")
    print("Zamek s           : ", s)
    print("Zamek t           : ", t)


def printhint( hint ):
    print("Prawidlowy wynik  : ", hint)


def printsol( sol ):
    print("Wynik algorytmu   : ", sol)


def check( G, s, t, hint, sol ):
    good = True

    if hint != sol:
        print("Błąd! Nieprawidlowy wynik algorytmu.")
        good = False

    return good

 
def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    #        0  1  2  3  4  5
    G = [ [ -1, 3, 8,-1,-1,-1 ],    # 0
          [  3,-1, 3, 6,-1,-1 ],    # 1
          [  8, 3,-1,-1, 5,-1 ],    # 2
          [ -1, 6,-1,-1, 7, 8 ],    # 3
          [ -1,-1, 5, 7,-1, 8 ],    # 4
          [ -1,-1,-1, 8, 8,-1 ]]    # 5
    s = 0
    t = 5
    hint = 25
    newtest = {}
    newtest["arg"] = [G,s,t]
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

