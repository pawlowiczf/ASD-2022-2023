from zad3testy import runtests

def Subsequenec(A, k):
    #
    n = len(A)
    maxLength = 1
    F = [ 0 for _ in range(k) ]

    for a in range(n):
        for b in range(a, n):
            F[ A[b] % k ]


def longest_incomplete( A, k ):
    # tu prosze wpisac wlasna implementacje
    return 0



runtests( longest_incomplete ) 
