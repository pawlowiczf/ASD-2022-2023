"""
Algorytm Kruskala wyznacza MST w czasie O( Elog*V ), gdyz uzylem kompresji sciezki i laczenia wedlug rank w strukturze Find-Union.
W zadaniu chodzi o znalezienie MST, ale takiego, ze dla kazdej krawedzi, ktora nie nalezy do MST, jej waga spelnia odpowiedni warunek.
W funkcji glownej 'beautree(G)' w petli 'for' tworze nowe drzewa MST, ale takie, ze kazde kolejne wybiera krawedzie z coraz mniejszego
zbioru, tj. zbioru, gdzie wagi krawedzi staja sie coraz wieksze. Dla kazdego takiego drzewa (jesli istnieje, tzn. len( MST ) = V - 1 ),
obliczam sume wag krawedzi i sprawdzam w funkcji 'CheckEdgeCondition', czy dla kazdej pozostalej krawedzi jest spelniony warunek. 
Zauwazmy, ze takie tworzenie drzewa MST z coraz mniejszego zbioru krawedzi spowoduje, ze krawedz o najmniejszej wadze w MST bedzie
coraz wieksza. W ten sposob sprawdze wszystkie potencjalne przypadki, gdy mamy rozne wagi krawedzi o najmniejszej i najwiekszej wadze w MST. 

- getEdgeList O( V + E )
- Kruskal O( Elog*V )
- checkEdgeCondition ( E * V ), gdyz len( MST ) --> V
- funkcja glowna 'beautree': O( E * E * log*V )

"""

from kol2testy import runtests

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0
    #
#end Class


def Find(x):
    #
    if x.parent != x:
        x.parent = Find( x.parent )
    #
    return x.parent
#end procedure Find()


def Union(X, Y): # X - root, Y - root 
    #
    if X.rank > Y.rank:
        Y.parent = X

    elif X.rank < Y.rank:
        X.parent = Y

    else:
        X.parent = Y 
        Y.rank += 1
#end procedure Union()


def Kruskal(G, Edges, i):
    index = i
    #
    n = len(G)
    minSpanningTree = []
    Vertices = [ Node(v) for v in range(n) ]

    sumMST = 0

    for edge in Edges[ i : len( Edges ) ]:
        #
        index += 1
        a, b, weight = edge
        rootA, rootB = Find( Vertices[a] ), Find( Vertices[b] )

        if rootA != rootB:
            Union( rootA, rootB )
            minSpanningTree.append( edge )
            sumMST += weight
        #end if 

        if len( minSpanningTree ) == n - 1: 
            return minSpanningTree, sumMST, index
    #end for
    return None, None, None
#end procedure Kruskal()


def getEdgesList(G):
    #
    edges = []

    for vertex in range( len(G) ):
        for (neighbour, weight) in G[vertex]:
            if vertex < neighbour:
                edges.append( (vertex, neighbour, weight) )
    #end 'for' loops

    return edges
#end procedure getEdgesList()


def checkEdgesCondition(Edges, minSpanningTree, minEdgeValue, maxEdgeValue, i):
    #
    #
    for edge in Edges[ i + 1 : i + len(minSpanningTree) ]:
        a, b, weight = edge 
        if minEdgeValue <= weight <= maxEdgeValue:
            return False 
            
    return True 
#end procedure checkEdges() 


def beautree(G):
    #
    n = len(G)

    Edges = getEdgesList(G)
    Edges.sort( key = lambda x: x[2] )
    minSumMST = float('inf') # suma wag krawedzi najmniejszego MST

    for i in range( len(Edges) ):
        #
        minSpanningTree, sumMST, index = Kruskal(G, Edges, i)

        if minSpanningTree != None: 
            #
            minEdgeValue = minSpanningTree[0][2]
            maxEdgeValue = minSpanningTree[n-2][2]

            if checkEdgesCondition( Edges, minSpanningTree, minEdgeValue, maxEdgeValue, i ):
                minSumMST = min( minSumMST, sumMST )
        
        #end 'if' clauses
    #end 'for' loop
    
    if minSumMST != float('inf'): return minSumMST
    return None
#end procedure beautree()

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
