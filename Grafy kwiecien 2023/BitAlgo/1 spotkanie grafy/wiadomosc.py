"""
Otrzymujemy na wejsciu liste par ludzi, ktore sie wzajemnie znaja. Osoby sa reprezentowane przez liczby od 0 do n - 1.
Dnia pierwszego osoba 0 przekazuje pewna wiadomosc wszystkim swoim znajomym. Dnia drugiego kazdy ze znajomych
przekazuje te wiadomosc wszystkim swoim znajomym, ktorzy jej jeszcze nie znali, i tak dalej
Algorytm, ktory zwroci dzien, w ktorym najwiecej osob poznalo wiadomosc oraz ilosc osob, ktore tego dnia ja otrzymaly.
"""

def addEdge(G, u, v):
    G[u].append(v)
    G[v].append(u)
#


def BFS(G, s):
    maxValue = 1  
    day = 1
    howManyAdded = 1 # ile wierzcholkow zostalo dodanych danego dnia np.

    visited = [False] * len(G)
    queue = []
    queue.append(s)
    visited[s] = True 

    while queue:
        #
        for _ in range(howManyAdded):
            s = queue.pop(0)
            howManyAdded = 0

            for vertex in G[s]:
                if visited[vertex] == False:
                    #
                    visited[vertex] = True
                    queue.append(vertex)
                    howManyAdded += 1
                    #
            #end for
        #
        currValue = len( queue )
        if currValue > maxValue: 
            maxValue = currValue
            whichDay = day 
        #
        day += 1
    #end while
    return whichDay, maxValue
#end for ^^^


V = 4
G = [ [] for _ in range(V) ]
addEdge(G,0,1)
addEdge(G,0,3)
addEdge(G,3,2)
addEdge(G,1,3)


whichDay, maxValue = BFS(G, 0)
print( whichDay, maxValue )


V = 14
G = [ [] for _ in range(V) ]
addEdge(G, 0, 1)
addEdge(G, 0, 2)
addEdge(G, 1, 2)
addEdge(G, 1, 3)
addEdge(G, 1, 4)
addEdge(G, 1, 5)
addEdge(G, 4, 5)
addEdge(G, 2, 6)
addEdge(G, 6, 7)
addEdge(G, 6, 8)
addEdge(G, 6, 9)
addEdge(G, 7, 13)
addEdge(G, 7, 10)
addEdge(G, 7, 11)
addEdge(G, 7, 12)
addEdge(G, 10, 13)

whichDay, maxValue = BFS(G, 0)
print( whichDay, maxValue )