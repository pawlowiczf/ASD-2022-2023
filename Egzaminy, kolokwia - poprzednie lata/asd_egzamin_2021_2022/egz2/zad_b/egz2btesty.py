# egz1atesty.py
from testy import *
from egz2btest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(*arg):
    print(f'C = {limit(arg[0])}')


def printhint( hint ):
    print("Poprawny wynik : ", limit(hint))


def printsol( sol ):
    print("Otrzymany wynik: ", limit(sol))


def check( hint, sol ):
    return hint==sol        	
 

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []
    
    C = [ [8, [ 6, 3], [ 4, 2], [7, 1]], # 0
        [22, [12, 2], [21, 3], [0,-1]], # 1
        [9, [11, 3], [ 0,-1], [7,-1]], # 2
        [15, [ 0,-1], [ 1,-1], [0,-1]] ] # 3    

    newtest = {}
    newtest["arg"] = [C]
    newtest["hint"] = 9
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

