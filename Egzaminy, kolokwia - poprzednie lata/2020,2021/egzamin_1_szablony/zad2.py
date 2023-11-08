from zad2testy import runtests
from queue import PriorityQueue

def Possible(L, y, x):
    #
    n = len(L)

    if 0 <= y < n and 0 <= x < n:
        if L[y][x] != "X":
            return True 
    #
    return False 
#end procedure Possible()


def Dijkstra(L, A, B):
    #
    n = len(L)
    moves = [ (0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1) ]
    times = [ 60, 45, 30, 45, 45 ]
    distance = [ [ [ float('inf') for _ in range( 12 ) ] for _ in range(n)  ] for _ in range(n) ]
    # 0 - pierwszy ruch do przodu (60 sek), 1 - drugi ruch do przodu (45 sek), 2 - trzeci ruch do przodu(30 sek), 3 - obrot w prawo (45 sek), 4 - obrot w lewo(45 sek)

    queue = PriorityQueue()
    queue.put( 0, A )

    y, x = A
    for a in range(5): distance[y][x] = 0

    while not queue.empty():
        #
        value, option, coords = queue.get()
        y, x = coords 

        
        for move in moves:
            a, b = move 
            a, b = a + y, b + x 

            



def robot( L, A, B ):
    #
    
    return 0

    
runtests( robot )


