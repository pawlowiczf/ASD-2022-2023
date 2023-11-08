# Dana jest szachownica o wymiarach n × n. Kazde pole (i, j)
# ma koszt (liczbe ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
# szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
# minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
# sciezki króla


# BFS, ktory traktuje wage, jako dodatkowe wierzcholki na sciezce miedzy rzeczywistymi wierzcholkami.

from collections import deque 


def isMovePossible(G, yTo, xTo):
    #
    n = len(G)

    if 0 <= yTo < n and 0 <= xTo < n:
        return True 
    return False 

#end procedure isMovePossible



def kingPath(G): # G - graf w postaci macierzowej
    #
    n = len(G)
    moves = [ (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1) ]

    parents  = [ [ None for _ in range(n) ] for _ in range(n) ]
    distance = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]
    distance[0][0] = 0

    queue = deque()
    queue.append( ( 1, (0, 0) ) )


    while queue:
        counter, vertex = queue.popleft()
        y, x = vertex 

        if counter == 1:
            
            for move in moves:
                toY, toX = move
                toY, toX = toY + y, toX + x

                if isMovePossible(G, toY, toX) and distance[ y ][ x ] + G[ toY ][ toX ] < distance[ toY ][ toX ]: 
                    queue.append( ( G[ toY ][ toX ], ( toY, toX ) ) )
                    distance[ toY ][ toX ] = distance[ y ][ x ] + G[ toY ][ toX ]
            #end for 

            if y == n - 1 and x == n - 1:
                return distance[y][x] + G[0][0]
            
        else:
            queue.append( ( counter - 1, vertex ) )

    #end while 
    return None
#end procedure 


G = [ [2, 2, 1, 5, 4],
[2, 1, 3, 1, 2],
[3, 1, 3, 5, 2],
[5, 4, 1, 5, 1],
[5, 3, 3, 4, 2] ]

print( kingPath(G) )


G = [ [5, 1, 5, 5, 1, 3, 4, 5, 1, 4, 5, 3],
[4, 4, 4, 2, 1, 1, 4, 1, 5, 3, 3, 4],
[5, 5, 3, 5, 1, 5, 5, 2, 5, 4, 1, 1],
[1, 5, 3, 1, 5, 2, 1, 3, 3, 5, 2, 1],
[1, 2, 3, 2, 5, 3, 5, 1, 3, 3, 2, 4],
[2, 2, 3, 5, 1, 4, 4, 1, 5, 1, 3, 2],
[1, 4, 2, 3, 3, 1, 1, 2, 1, 5, 2, 5],
[2, 5, 3, 4, 1, 5, 2, 5, 3, 2, 2, 1],
[2, 4, 5, 5, 5, 1, 3, 3, 1, 5, 1, 2],
[2, 4, 4, 3, 1, 2, 1, 3, 1, 2, 2, 4],
[5, 4, 3, 5, 3, 5, 1, 5, 2, 3, 1, 3],
[5, 5, 1, 3, 5, 4, 2, 3, 5, 3, 2, 3] ]

print( kingPath(G) )