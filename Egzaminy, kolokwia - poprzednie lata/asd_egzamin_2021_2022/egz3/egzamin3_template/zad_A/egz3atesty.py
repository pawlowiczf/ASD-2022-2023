# egz3atesty.py
from testy import *
from egz3atest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(*arg):
    print(f'T = {limit(arg[0])}')
    print(f'I = {limit(arg[1])}')


def printhint( hint ):
    print("Poprawny wynik: ", limit(hint))


def printsol( sol ):
    print("Otrzymany wynik: ", limit(sol))


def check( hint, sol ):
    return hint==sol        	
 

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []
    
    T = 100
    I = [(3, 10), (0, 5), (20, 30), (25, 35), (26, 26)]
    newtest = {}
    newtest["arg"] = [T, I]
    newtest["hint"] = 3
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

