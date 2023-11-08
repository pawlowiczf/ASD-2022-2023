# zad5testy.py
from testy import *
from zad5test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(T):
    print("Pola ropy                  : ", limit(T))


def printhint( hint ):
    print("Oczekiwana liczba postojow : ", hint )


def printsol( sol ):
    print("Otrzymana licza postojow   : ", limit(len(sol)))
    print("Otrzymane postoje          : ", limit(sol))


def check( T, hint, sol ):
    if len(sol) > hint:
      print("Blad! Za duzo postojow")
      return False
      
    for i in range(1, len(sol)):
      if sol[i-1] >= sol[i]:
        print("Blad! Lista postojow nie jest posortowana rosnaco")
        return False

    n = len(T)
    F = [False for i in range(n)]
    for i in sol: F[i] = True
    
    B = 0
    for i in range(n):
      if B < 0:
        print(f"Blad! Zabraklo paliwa na dojazd do pola {i}")      
        return False
      if F[i]: B += T[i]
      B -= 1
     
    return True
    
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

