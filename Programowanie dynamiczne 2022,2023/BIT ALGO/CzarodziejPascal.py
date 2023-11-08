"""
f(i, k) - maksymalna pieknosc po wzieciu 'i' talerzy z 'k' pierwszysch stosow 
i - liczba talerzy 
k - liczba pierwszych stosow 

f(i, k) = max( f(i - j, k - 1) + E P[k][h], gdzie h od <1, j>
gdzie j od <0, i>
"""

def reMap( stack ):
    #
    for k in range( 1, len(stack) ):
        stack[k] += stack[k-1]
    #
#end procedure reMap()


def Plates( stacks, P ):
    #
    n = len( stacks )
    k = len( stacks[0] )
    F = [ [ 0 for _ in range( n ) ] for _ in range(P + 1) ]

    if k * n  < P: return -1 # za duzo gosci 

    for stack in stacks:
        reMap(stack)
    #

    for plate in range( min( P , k ) + 1 ):
        F[plate][0] = stacks[0][plate - 1]
    #

    for stack in range(n):
        for plates in range(P + 1):

            F[plates][stack] = F[plates][stack - 1]

            for j in range(1, min(plates, k) + 1): # min(plates, k), bo nie mozemy wziac wiecej talerzy niz jest na stosie 'stack'
                sumBeauty = stacks[ stack ][j - 1]
                F[plates][stack] = max( F[plates][stack], F[plates - j][stack - 1] + sumBeauty )
            #end 'for' loop

    #end 'for' loops 

    return F[P][n - 1]
#end procedure Plates()


plates = [
    [1, 8, 2, 3, 0, 9],
    [3, 0, 0, 1, 20, 33],
    [10, 1, 8, 1, 9, 5],
    [7, 6, 2, 8, 4, 3],
]
guests = 8  
print( Plates(plates, guests) ) # 74 


plates = [
    [1, 8, 2, 3, 0, 9],
    [3, 0, 0, 1, 20, 33],
    [10, 1, 8, 1, 9, 5],
    [7, 6, 2, 8, 4, 3],
]
guests = 17
print( Plates(plates, guests) ) # 118
