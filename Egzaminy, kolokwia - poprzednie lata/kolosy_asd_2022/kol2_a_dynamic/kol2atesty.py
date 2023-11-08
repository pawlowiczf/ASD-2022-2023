# zad5testy.py
from testy import *
from kol2atest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(P, B):
    P = [ f"{i}:{p}" for i,p in enumerate(P) ]
    print("Punkt B : ", B )
    print("Punkty  : ", limit(", ".join(P))  )


def printhint( hint ):
    pass

def printsol( sol ):
    print("Otrzymane punkty zmian : ", limit(sol))


def check( P, B, hint, sol ):
    CHG = [ (i,P[i]) for i in sol ]
    for (i,p) in CHG:
      if p[1] == False:
        print(f"Blad! Punkt {i} ({p}) nie jest punktem przesiadkowym")
        return False      
    
    C = [ P[i][0] for i in sol ]
    C.sort()
    P.sort()
    
    D  = 0 # Jacek
    MC = 0 # punkty kontrolne przejechane przez Mariana
    j  = 0 # ile punktow zmiany minelismy od ostatniej zmiany
    i  = 0 # aktualny mozliwy punkt zmiany
    
    for (x,t) in P:
      # punkt kontrolny
      if t == False:
        if D == 1: MC += 1
      # punkt zmiany        
      if t == True: 
        j += 1
        if j == 4: 
          print("Blad! Wiecej niz trzy punkty przesiadkowe bez zmiany")
          return False
        if i < len(C) and C[i] == x:
          D = 1-D 
          j = 0
          i += 1
        
    print("Oczekiwane punkty kontrolne Mariana: ", hint )        
    print("Otrzymane punkty kontrolne Mariana : ", MC)
        
          
    if MC > hint:
      print("Blad! Marian jedzie przez zbyt wiele punktow kontrolnych")
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

