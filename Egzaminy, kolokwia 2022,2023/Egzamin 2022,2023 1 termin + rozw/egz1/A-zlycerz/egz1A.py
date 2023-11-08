"""
Filip Pawlowicz 414324 
Algorytm zlozonosc akceptowalna V^3 log V
W funkcji glownej dla kazdego wierzcholka V (zakladam, ze to jest wierzcholek, ktory zly rycerz obrobi ), puszczam
dwa wywolania algorytmu Dijkstry: 1 - najkrotsza sciezka z wierzcholka s do V, 2 - najkrotsza sciezka z wiercholka V do t.
Na koncu sumuje te wartosci i odejmuje zloto, ktore zostalo zdobyte w zamku V. 
W ten sposob uzyskam najefektywniejszy sposob dotarcia do wierzcholka t ( sprawdze po prostu wszystkie opcje ).
Flaga True - sciezka idzie juz po obrobieniu zamku (wiekszy koszt wag krawedzi)
Flaga False - sciezka, ale jeszcze nie zaatakowalem zamku (koszt normalny)
Jeszcze wywoluje poza petla ponownie Dijkstre, ale zakladajac ze nie obrabim zadnego zamku.
Wynik zwracam. 
"""

from egz1Atesty import runtests
from queue import PriorityQueue

def Dijkstra(G, V, s, t, r, flag):
  #
  n = len(G)
  distance = [ float('inf') for _ in range(n) ]

  queue = PriorityQueue()
  queue.put( (0, s) )
  distance[s] = 0

  while not queue.empty():
    #
    value, vertex = queue.get()

    if vertex == t:
      break

    if flag:

      for neighbour, weight in G[vertex]:

        if distance[vertex] + 2 * weight + r < distance[neighbour]:
          distance[neighbour] = distance[vertex] + 2 * weight + r 
          queue.put( (distance[neighbour], neighbour) )

      #end 'for' loop

    else:

      for neighbour, weight in G[vertex]:

        if distance[vertex] + weight < distance[neighbour]:
          distance[neighbour] = distance[vertex] + weight
          queue.put( (distance[neighbour], neighbour) )        

      #end 'for' loop 
  #end 'while' loop

  return distance[t]
#end procedure Dijkstra()

def gold(G,V,s,t,r):
  #
  n = len(G)
  minValue = float('inf')

  for vertex in range( len(G) ): 
    profit = V[vertex]
    value = Dijkstra(G, V, s, vertex, r, False) + Dijkstra(G, V, vertex, t, r, True)

    value -= profit
    minValue = min( minValue, value )
  #end 'for' loop

  minValue = min( minValue, Dijkstra(G, V, s, t, r, False) )
  return minValue
#end procedure gold()


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
