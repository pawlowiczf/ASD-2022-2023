"""
Dany jest graf G = (V,E), którego wierzchołki reprezentuja punkty
nawigacyjne nad Bajtocja, a krawedzie reprezentuja korytarze powietrzne miedzy tymi punktami. Kazdy
korytarz powietrzny ei > E powiazany jest z optymalnym pułapem przelotu pi > N (wyrazonym w metrach).
Przepisy dopuszczaja przelot danym korytarzem jesli pułap samolotu rózni sie od optymalnego najwyzej o t
metrów. Prosze zaproponowac algorytm (bez implementacji), który sprawdza czy istnieje mozliwosc przelotu
z zadanego punktu x > V do zadanego punktu y > V w taki sposób, zeby samolot nigdy nie zmieniał pułapu.

"""


def DFS(G, visited, path, t, source, destination, height):
    #
    visited[source] = True
    path.append(source)

    if source == destination:
        print( path ) 
    
    else:

        for (neighbour, optimal) in G[source]:

            if visited[neighbour] == False and abs( height - optimal ) < t:
                DFS(G, visited, path, t, neighbour, destination, height)
        #end for 
    #
    visited[source] = False 
    path.pop()

#end procedure ^^^     

def check(G, n):
    visited = [ False for _ in range(n) ]
    path = []

    for a in range(n - 1):
        for b in range( a + 1, n):
            DFS(G, visited, path, t, a, b, 8 )
    #end for's

#end procedure




G = [[(1, 10), (2, 7), (3, 3)], [(0, 10), (3, 5), (4, 20)], [(0, 7), (4, 11), (7, 8)],
         [(0, 3), (1, 5), (4, 14), (5, 5)], [(1, 20), (2, 11), (3, 14), (6, 8)], [(3, 5), (6, 9)],
         [(4, 8), (5, 9), (7, 13)], [(2, 8), (6, 13), (8, 10)], [(7, 10)]]
t = 3  

check(G, len(G) )