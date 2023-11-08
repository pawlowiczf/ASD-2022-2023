# Rozwiazanie za pomoca tablicy znajduje sie w folderze Grafy
# Ponizej rozwiazanie z wykorzystaniem macierzy incydencji 

def Path(G, s):
    n = len( G[0] )

    visited = [ False for _ in range(n) ]
    parent =  [ None for _ in range(n)     ]
    queue = []

    queue.append(s)
    visited[s] = True 

    while queue:
        s = queue.pop(0)

        for v in range(n):
            if G[s][v] == 1 and visited[v] == False:
                visited[v] = True 
                parent[v]  = s
                queue.append(v)
        #
    #end while 
    return visited, parent 
#end def ^^^

def PathRek(G, u, v, parent):
    if u == v: print(u)
    else: 
        PathRek(G, u, parent[v], parent)
        print(v)
#


def shortestPath(G, u, v):
    visited, parent = Path(G, u)
    
    if visited[v] == False: return False 
    else: PathRek(G, u, v, parent)
#end def ^^^



G = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

shortestPath(G, 0, 9)



