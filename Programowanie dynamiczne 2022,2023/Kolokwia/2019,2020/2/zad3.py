from zad3testy import runtests

def CommonDigit(a, b):
    #
    Digits = [ False for _ in range(10) ]

    while a > 0:
        Digits[ a % 10 ] = True 
        a = a // 10
    #

    while b > 0:
        if Digits[ b % 10 ]: return True 
        b = b // 10 
    #

    return False 
#end procedure CommonDigit()


def Jump(P):
    #
    n = len(P)
    F = [ float('inf') for _ in range(n) ]
    F[0] = 0
    P.sort()

    for a in range(1, n):
        for b in range(a):
            if CommonDigit( P[a], P[b] ):
                F[a] = min( F[a], F[b] + P[a] - P[b] )
    #end 'for' loops 

    return F[n - 1]
#end procedure Jump()


def find_cost(P):
    #
    answer = Jump(P)
    return answer if answer != float('inf') else -1
#end procedure find_cost()


runtests(find_cost) 
