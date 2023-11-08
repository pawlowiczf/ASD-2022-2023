# egz1Atesty.py
from testy import *
from egz1Atest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(*arg):
    print(f'G={limit(arg[0])}')
    print(f'V={limit(arg[1])}')
    print(f's={arg[2]}')
    print(f't={arg[3]}')
    print(f'r={arg[4]}')

def printhint( hint ):
    print("Poprawny wynik  : ", limit(hint) )

def printsol( sol ):
    print("Otrzymany wynik : ", limit(sol) )


def check( hint, sol ):
    return hint==sol        	
 
    
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

