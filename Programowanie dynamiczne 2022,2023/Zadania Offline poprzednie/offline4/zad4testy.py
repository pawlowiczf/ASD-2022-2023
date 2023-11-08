# zad3testy.py
from testy import *
from zad4test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(T, p):
    print("Budynki               :\t", limit(T))
    print("Budzet                :\t", p )


def printhint( hint ):
    print("Oczekiwana pojemnosc  :\t", hint )


def printsol( sol ):
    print("Wyjście algorytmu     :\t", limit(sol))


def check( T, p, hint, sol ):

    B = []
    for i in sol:
      B.append(T[i])
    B.sort( key = lambda x: x[1])
        
    # sprawdz, czy budynki na siebie nachodza
    for i in range(1,len(B)):
      if B[i-1][2] >= B[i][1]:
        print("Blad! Budynki na siebie zachodza: ", B[i-1], B[i] )
        return False
        
    students = 0 
    cost     = 0
    for i in range(len(B)):
      students += (B[i][2]-B[i][1])*B[i][0]
      cost     += B[i][3]

    print("Pojemnosc rozwiazania :\t", students)
    print("Koszt rozwiazania     :\t", cost )
    
    if cost > p:
      print("Blad! Rozwiazanie zbyt drogie")
      return False
      
    if students < hint:
      print("Blad! Rozwiazanie miesci zbyt malo studentow")
      return False



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

