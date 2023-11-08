def cuttingRod(P, n): # n - dlugosc preta 
    #
    F    = [ -float('inf') for _ in range(n + 1) ]
    prev = [ None for _ in range(n + 1) ]

    F[0] = 0

    for k in range(1, n+1):
        for i in range(k+1):
            
            if F[k-i] + P[i] > F[k]:
                F[k] = F[k-i] + P[i]
                prev[k] = k - i 
    #end 'for' loops 

    return restoreRods(prev, n)
#end procedure cuttingRod()

def restoreRods(prev, n):
    #
    
    while prev[n] != None:
        #
        rodLength = n - prev[n] 
        print(rodLength, end = " ")
        n = prev[n] 
    #end 'while' loop 
    print()
#end restoreRods


P = [0, 1, 3, 6, 5, 3] 
n = 5
cuttingRod(P, n)

P = [0, 2, 1, 1, 2, 1, 12, 11, 11, 11, 13, 11, 19, 32, 23, 24, 19, 20]
n = 17
cuttingRod(P, n)