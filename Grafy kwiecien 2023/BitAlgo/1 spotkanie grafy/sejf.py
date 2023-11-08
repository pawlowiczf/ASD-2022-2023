"""
Dostales sejf, ktory odblokowuje sie czterocyfrowym Pinem( 0000-9999 ). Pod wyswietlaczem
znajduje sie kilka przyciskow z liczbami od 1 do 9999 - przykladowo (13, 223, 782, 3902). Sejf
ten dziala inaczej niz normalny: wcisniecie przycisku powoduje dodanie liczby z przycisku do
liczby na wyswietlaczu. Jezeli suma jest wieksza niz 9999, to pierwsza cyfra zostaje obcieta.

Jest tobie znany PIN oraz cyfry, ktore sa aktualnie wyswietlane. Znajdz najkrotsza sekwencje nacisniec przyciskow,
ktora pozwoli Ci odblokowac sejm. Jezeli nie istnieje taka sekwencja, zwroc None. 

"""

from collections import deque

def BFS(currentNumberDisplayed, numbers, PIN):
    n = 10000
    #
    visited = [ False for _ in range(n) ]
    parent  = [ None for _ in range(n)  ]
    queue = deque()

    queue.append( currentNumberDisplayed )
    visited[ currentNumberDisplayed ] = True 

    while queue:
        vertex = queue.popleft()
        
        for neighbour in numbers:

            newVertex = ( vertex + neighbour ) % 10000 

            if visited[ newVertex ] == False:
                visited[ newVertex ] = True
                parent[ newVertex ] = vertex 
                queue.append( newVertex )
            
        if newVertex == PIN:
            return parent
            
        #end for 
    #end while 
    return None

#end procedure BFS()


def shorthestCombination(currentNumberDisplayed, numbers, PIN):
    #
    parent = BFS(currentNumberDisplayed, numbers, PIN)
    path = []

    if parent == None: return None 
    destination = PIN

    while destination != currentNumberDisplayed:
        path.append( ( destination - parent[destination] ) % 10000 )
        destination = parent[ destination ]
    #end while 
    path.reverse()
    return path 

#end procedure shorthestCombination()

PIN = 1337 
NUM = 1234 

buttons = [13, 223, 782, 3902]

print( shorthestCombination(NUM, buttons, PIN) )

