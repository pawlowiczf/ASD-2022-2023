# Dobry poczatek
# Wierzchołek v w grafie skierowanym nazywamy dobrym poczatkiem jesli
# kazdy inny wierzchołek mozna osiagnac sciezka skierowana wychodzaca z v. Prosze podac algorytm, który
# stwierdza czy dany graf zawiera dobry poczatek.


"""
Znajdz wszystkie spojne skladowe, zamien je na jeden wierzcholek
Silna spojna skladowa to taki podzbior wierzcholkow ze istnieje sciezka pomiedzy kazda para wierzcholkow w tej 
silnie spojnej skladowej
bo w cyklu kazdy wierzcholek jest dobrym poczatkiem 

Z dfs:
- dfs na grafie (petla, dla kazdego wierzcholka, az nie odwiedzimy kazdego) 
- zapisujemy kolejnosc przetwarzania (postorder)
- znajdujemy wierzcholek z najwyzsza wartoscia i z tego wierzcholka robimy dfs lub bfs, aby sprawdzic
czy mozemy z niego dotrzec do kazdego innego wierzcholka. Jesli tak, to znalezlismy dobrym poczatkiem

Z 
Odwracasz krawedzie 
Sortujesz topologicznie,
"""

def addEdge(n, edges):
    G = [ [] for _ in range(n) ]
    for edge in edges:
        a = edge[0]
        b = edge[1]
        G[a].append(b)
        G[b].append(a)
    #
    return G
#end def ^^^


def DFS(G, n, v, visited, departure, time):
    visited[v] = True

    for vertex in G[v]:
        if visited[vertex] == False:
            time = DFS(G, n, vertex, visited, departure, time)
    #end for 

    time += 1
    departure[v] = time 
    return time 

#end def ^^^

def DfsDriver(G, n):
    visited = [ False for _ in range(n) ]
    departure = [ -1 for _ in range(n) ]
    time = 0

    for v in range(n):
        if visited[v] == False:
            time = DFS(G, n, v, visited, departure, time)


    maxVertex = departure.index( len(G) ) # wierzcholek, ktory zostal przetworzony, jako ostatni

    visited = [ False for _ in range(n) ]
    departure = [ -1 for _ in range(n) ]
    time = 0
    time = DFS(G, n, maxVertex, visited, departure, time)

    for v in range(n):
        if visited[v] == False:
            return False 
    #
    return True 
#end def ^^^


edges = [ (0, 1), (0, 2), (1, 2), (1, 3), (1, 5), (2, 4), (4, 3) ]
n = 6
G = addEdge(n, edges)
departure = DfsDriver(G, n)
print(departure)