"""
Dany jest graf G = (V,E), gdzie kazda krawedz ma wage ze zbioru
{1, . . . , E} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla danych wierzchołków
x i y sprawdza, czy istnieje sciezka z x do y, w której przechodzimy po krawedziach o coraz mniejszych wagach.

Dodatkowy argument, ktory mowi o wadze ostatniej krawedzi.
Robimy przeszukanie dla wszystkich krawedzi, ktore maja wage mniejsza
Nie mamy visted, mozemy wchodzic do wierzcholkow kilka razy 
Nie zapetlimy sie, nie cofniemy sie, bo wchodzimy do krawedzi o MNIEJSZEJ wadze 
Wagi sa tez parami rozne 

"""

def DFS(G, value, source, destination):
    
    for (neighbour, weight) in G[source]:
        #
        if neighbour == destination and value > weight:
            return True 

        elif value > weight:
            if DFS(G, weight, neighbour, destination):
                return True
                
        # 
    #end for 

    return False 
#end procedure ^^^

def createG(edges, n):
    G = [ [] for _ in range(n) ]

    for edge in edges:
        a, b, value = edge[0], edge[1], edge[2]
        G[a].append( (b, value) )
        G[b].append( (a, value) )
    #end for 
    return G
#end procedure ^


edges = [(0, 1, 12), (0, 2, 7), (1, 0, 12), (1, 3, 13), (1, 4, 9), (2, 0, 7), (2, 3, 2), (2, 5, 4),
         (3, 1, 13), (3, 2, 2), (3, 4, 10), (3, 5, 3), (4, 1, 9), (4, 3, 10), (4, 6, 10), (5, 2, 4),
         (5, 3, 3), (5, 6, 2), (6, 4, 10), (6, 5, 2)]
G = createG(edges, 7)

print( DFS(G, float('inf'), 0, 6) )

edges = [ (0, 1, 6), (1, 3, 4), (3, 4, 5), (2, 4, 2), (0, 2, 6), (0, 3, 1), (1, 4, 9), (1, 2, 5) ]
G = createG(edges, 5)
print( DFS(G, float('inf'), 0, 4) )

edges = [ (0, 3, 10), (3, 4, 11), (4, 5, 5), (0, 1, 11), (1, 2, 9), (2, 5, 10)  ]
G = createG(edges, 6)
print( DFS(G, 5, 0, float('inf') ) )


# Inne rozwiazanie:

# def DFS(G, end, vertex, lastWeight):

#     if vertex != end:
#         for (neighbour, weight) in G[vertex]:
#             if weight < lastWeight:

#                 if DFS(G, end, neighbour, weight):
#                     return True 
#         #end for 
#         return False 
#     #
#     return True 
# #end procedure DFS()