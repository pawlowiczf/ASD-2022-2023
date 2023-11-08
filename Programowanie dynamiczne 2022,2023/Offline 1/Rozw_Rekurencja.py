from zad7testy import runtests

class MazeData:
    def __init__(self, L, n):
        self.L = L
        self.moves = [ (1, 0), (0, 1), (-1, 0) ]
        self.n = n
        self.visited = [ [ False for _ in range(n) ] for _ in range(n) ]
        self.F = [ [ -float('inf') for _ in range(n) ] for _ in range(n) ]
        self.bestResult = 0
#end Class

def Possible(L, y, x):
    #
    n = len(L)

    if 0 <= y < n and 0 <= x < n:
        if L[y][x] == ".":
            return True  
    #
    return False 
#end procedure Possible()


def Travel( Maze, n, y, x, counter):
    #
    Maze.visited[y][x] = True 

    if y == n - 1 and x == n - 1:

        Maze.bestResult = max( Maze.bestResult, counter )
        Maze.visited[y][x] = False 
        return counter
    
    #end 'if' clause 


    for (a, b) in Maze.moves:
        newY, newX = y + a, x + b 

        if Possible(Maze.L, newY, newX) and not Maze.visited[newY][newX]:
            Travel( Maze, n, newY, newX, counter + 1)
        #
    #end 'for' loop

    Maze.visited[y][x] = False
#end procedure Travel()

    
def maze( L ):
    #
    Maze = MazeData(L, len(L) )
    Travel(Maze, len(L), 0, 0, 0)
    
    return Maze.bestResult
#end procedure maze()

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )


