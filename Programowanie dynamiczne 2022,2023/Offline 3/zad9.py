from zad9testy import runtests
"""
Funkcja dynamiczna F(station, flag)
Flag == 1: dotarlem do stacji 'station' wykorzystujac wyjatek (teraz, badz wczesniej)
Flag == 0: dotarlem do stacji 'station' nigdy nie wykorzystujac wyjatku

"""

def mapArray(T, C, L):
    #
    for a in range( len(T) ):
        T[a] = (C[a], T[a])
    #

    T.append( (0, 0) )
    T.append( (0, L) )
    T.sort( key = lambda x: x[1] )
    return T
#end procedure mapArray() 


def Traverse(O, C, T, L):
    #
    O = mapArray(O, C, L)
    n = len(O)
    F = [ [ float('inf') for _ in range(2) ] for _ in range(n) ]
    
    F[0][0] = 0 
    F[0][1] = 0

    if T >= L: return 0

    for station in range(1, n):

        for neighbour in reversed( range(station) ):

            if O[station][1] - O[neighbour][1] <= T: 
                F[station][0] = min( F[station][0], F[neighbour][0] + O[station][0] )
                F[station][1] = min( F[station][1], F[neighbour][1] + O[station][0] )

            elif O[station][1] - O[neighbour][1] <= 2 * T:
                F[station][1] = min( F[station][1], F[neighbour][0] + O[station][0] )

            else: break
        # 
    #end 'for' loop 

    return min( F[n - 1][0], F[n - 1][1] )
#end procedure Traverse()
    
def min_cost( O, C, T, L ):
    #
    return Traverse(O, C, T, L)
#end procedure min_cost()

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )

