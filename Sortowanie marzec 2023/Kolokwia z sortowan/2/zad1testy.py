# zad1testy.py
from testy import *
from zad1test_spec import ALLOWED_TIME, TEST_SPEC

from copy import deepcopy


class Node:
  def __init__(self):
    self.val = None
    self.next = None


def tab2list(t):
    n = len(t)
    p = None

    for i in range(n-1,-1,-1):
        q = Node()
        q.val = t[i]
        q.next = p
        p = q

    return p


def list2tab(l):
    t = []
    while l!=None:
        t.append(l.val)
        l = l.next

    return t


def copyarg( arg ):
    #return deepcopy(arg)

    (l, k) = arg

    q = Node()
    q.val = l.val
    head = q
    l = l.next

    while l is not None:
        q.next=Node()
        q = q.next
        q.val = l.val
        l = l.next

    return (head, k)


def printarg(L, k):
    print(f"k: {k}")
    out = ', '.join([str(x) for x in list2tab(L)])
    print("Wejciowa lista:\t", limit(out))


def printhint( hint ):
    out = ', '.join([str(x) for x in hint])
    print("Lista posortowana:\t", limit(out))


def printsol( sol ):
    out = ', '.join([str(x) for x in list2tab(sol)])
    print("Wynik algorytmu:\t", limit(out))

 
def check( l, k, hint, sol ):
    good = True

    t = list2tab(sol)
    if len(hint) != len(t):
        print("Błąd! Nieprawidlowa liczba elementow w wyniku")
        good = False
    else:
        for i, elem in enumerate(zip(hint, t)):
            if elem[0] != elem[1]:
                print(f'Błąd! Nieprawidlowa liczba na pozycji {i}')
                good = False
                break

    return good


def gentest(k, n, maxint):
    l = [MY_random() % maxint for i in range(n)]
    l = sorted(l)
    pos = [i for i in range(n)]

    for i in range(n):
        if pos[i] != i: continue

        j = i + (MY_random() % (k+1))
        if j < n and pos[j] == j:
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp
            tmp = pos[i]
            pos[i] = pos[j]
            pos[j] = tmp

    arg = (tab2list(l), k)
    hint = sorted(l)
    return arg, hint


def runtests( f ):
    TESTS = []
    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    internal_runtests( copyarg, printarg, printhint, printsol, check, TESTS, f, ALLOWED_TIME )

