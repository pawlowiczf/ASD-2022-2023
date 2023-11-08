def possibleNeighbour(G, y, x):
    n = len(G)
    if 0 <= y < n and 0 <= x < n:
        return True
    return False
#end def ^^^


def BFS(G, y, x, visited):
    lakeBig = 1
    queue = []
    queue.append( (y, x) )
    visited[y][x] = True
    neighbours = [ (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1) ]

    while queue:
        y, x = queue.pop(0)

        for vertex in neighbours:
            if possibleNeighbour(G, y + vertex[0], x + vertex[1]) and G[ y + vertex[0] ][ x + vertex[1] ] == 1:
                if visited[ y + vertex[0] ][ x + vertex[1] ] == False:
                    queue.append( ( y + vertex[0], x + vertex[1] ) )
                    visited[ y + vertex[0] ][ x + vertex[1] ] = True
                    lakeBig += 1
            #
        #end for

    #end while
    return lakeBig
#end def ^^^


def lakes(G):
    maxLakeBig = 0
    n = len(G)
    visited = [ [False for _ in range(n)] for _ in range(n) ]
    counter = 0
    #

    for y in range(n):
        for x in range(n):
            if visited[y][x] == False and G[y][x] == 1:
                lakeBig = BFS(G, y, x, visited)
                counter += 1
                maxLakeBig = max( lakeBig, maxLakeBig )
    #end for's

    return counter, maxLakeBig
#end def ^^^


G = [ [0, 1, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 1, 0],
      [0, 1, 1, 1, 1, 0, 1, 0],
      [0, 0, 1, 1, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 1, 0],
      [1, 1, 0, 1, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 0, 0, 0] ]

#Podpunkt a) i b):

number, maxLakeBig = lakes(G)
print(number)
print(maxLakeBig)

# --------------------------

def DFS(G, visited):
    n = len(G)
    stack = []
    stack.append( (0,0) )
    visited[0][0] = True
    #
    neighbours = [ (-1,0), (0,1), (1,0), (0,-1) ]

    while stack:
        y, x = stack.pop()
        for vertex in neighbours:
            if possibleNeighbour( G, y + vertex[0], x + vertex[1] ) and G[ y + vertex[0] ][ x + vertex[1] ] == 0:
                if visited[ y + vertex[0] ][ x + vertex[1] ] == False:
                    visited[ y + vertex[0] ][ x + vertex[1] ] = True
                    stack.append( ( y + vertex[0], x + vertex[1] ) )
        #end for
        if visited[n-1][n-1]:
            return True
    
    #end while
    return False
#end def ^^^


def RecursiveDFS(G):
    n = len(G)
    visited = [ [False for _ in range(n)] for _ in range(n) ]
    return DFS(G, visited)
#end def ^^^

def pathBFS(G):
    n = len(G)
    visited = [ [False for _ in range(n) ] for _ in range(n) ]
    pathLength = [ [0 for _ in range(n) ] for _ in range(n) ]
    neighbours = [ (-1,0), (0,1), (1,0), (0,-1) ]
    #
    queue = []
    queue.append( (0,0) )
    visited[0][0] = True

    while queue:
        y, x = queue.pop(0)

        for vertex in neighbours:
            if possibleNeighbour( G, y + vertex[0], x + vertex[1] ) and G[ y + vertex[0] ][ x + vertex[1] ] == 0:
                if visited[ y + vertex[0] ][ x + vertex[1] ] == False:
                    visited[ y + vertex[0] ][ x + vertex[1] ] = True
                    queue.append( (y + vertex[0], x + vertex[1] ) )
                    pathLength[ y + vertex[0] ][ x + vertex[1] ] += pathLength[y][x] + 1
        #end for
    #end while
    return pathLength[n-1][n-1]         
#end def ^^^

#Podpunkt c) i d):
print( RecursiveDFS(G) ) #podpunkt C
print( pathBFS(G) )


