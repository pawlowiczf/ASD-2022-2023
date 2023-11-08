"""
Prosze zaimplementowac algorytm obliczajacy domkniecie przechodnie
grafu reprezentowanego w postaci macierzowej (domkniecie przechodnie grafu G, to graf nad tym
samym zbiorem wierzchołków, który dla kazdych dwóch wierzchołków u i v ma krawedz z u do v wtedy i
tylko wtedy, gdy w G istnieje sciezka z u do v.

Mamy graf skierowany, w postaci macierzowej, i chcemy podokładać krawędzie między wierzcholkami (u,v), wtedy
gdy miedzy wierzcholkami (u,v) istnieje sciezka.
"""

"""
Zaczynamy od kazdego wierzcholka osobno ( DFS ? ). Da nam to zbior wierzcholkow osiagalnych z danego. 
Musimy wziac pod uwage ewentualne cykle, ktore prowadza z powrotem. 
Zastosuj Floyd-Warshall. Wykorzystaj strukture tego algorytmu. 
Jesli potrafimy znalezc najkrotsze odleglosci miedzy kazda para algorytmow, to jesli jakas sciezka jest
i mamy jakas liczbe to wiemy ze sciezka istnieje i 'inf', gdy sciezki nie ma. True / False w tym przypadku.

Graf reprezentowany w postaci macierzowej: G = [ F, T, F, F 
                                                 F, F, T, F ] itd. 

                                                 
"""

def domkniecie(G):
    n = len(G)

    distance = [ [ 0 for _ in range(n) ] for _ in range(n) ]


    for t in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = ( G[i][t] and G[t][j] ) or G[i][j]
    #
    return G
#end procedure domkniecie()           

# -------------------
"""
Below are the abstract steps of the algorithm. 

Create a matrix tc[V][V] that would finally have transitive closure of the given graph. Initialize all entries of tc[][] as 0.
Call DFS for every node of the graph to mark reachable vertices in tc[][]. In recursive calls to DFS, we don’t call DFS for an adjacent vertex if it is already marked as reachable in tc[][].
Below is the implementation of the above idea. The code uses adjacency list representation of input graph and builds a matrix tc[V][V] such that tc[u][v] would be true if v is reachable from u.
"""
def createG(n, edges):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a, b = edge
        G[a].append(b)
    #
    return G
#end procedure create()



def DFS(G, cMatrix, source, descendant):
    #
    for neighbour in G[descendant]:

        if cMatrix[source][neighbour] == 0:
            cMatrix[source][neighbour] = 1
            DFS(G, cMatrix, source, neighbour)
        #
    #end for
#end procedure DFS()

def cMatrixAlgorithm(G):
    #
    n = len(G)
    cMatrix = [ [ 0 for _ in range(n) ] for _ in range(n) ]

    for vertex in range(n):
        cMatrix[vertex][vertex] = 1
        DFS(G, cMatrix, vertex, vertex)
    #end for 
    return cMatrix

#end procedure cMatrixAlgorithm()

# edges = [(0, 2), (1, 0), (3, 1)]
# n = 4
# G = createG(n, edges)
# cMatrix = cMatrixAlgorithm(G)
# for y in cMatrix: print(y)

# ------------------



