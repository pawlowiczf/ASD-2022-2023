from zad3testy import runtests
# F[i] - minimalna liczba zatrzyman wyruszajac ze stacji 'i' 

class CreateData:
    def __init__(self, T, V, q, l):
        self.T = T
        self.V = V
        self.q = q 
        self.l = l 
        self.F = [ float('inf') for _ in range( len(T) ) ]
        self.parent = [ None for _ in range( len(T) ) ]
        self.n = len(T)
#end Class 


def restoreStations(Data):
    #
    result = [] 
    n = Data.n
    if Data.parent[n - 1] == None: return []

    a = n - 1
    while a != None:
        result.append(a)
        a = Data.parent[a] 
    #

    result.reverse()
    return result 
#end procedure restoreStations()


def Traverse(Data, a, fuel):
    #
    if a == Data.n - 1: 
        Data.F[a] = 0
        return 0 
    #
    if a >= Data.n:
        return float('inf')
    #

    if Data.F[a] == float('inf'):
        fuel += Data.V[a] 

        for neighbour in range(a + 1, Data.n):
            if Data.T[neighbour] > Data.T[a] + fuel: break 

            if fuel - ( Data.T[neighbour] - Data.T[a] ) > 0:
                value = 1 + Traverse(Data, neighbour, fuel - ( Data.T[neighbour] - Data.T[a] ) )
                if value < Data.F[a]:
                    Data.F[a] = value 
                    Data.parent[neighbour] = a 
            #
        #end 'for' loop 
    #end 'if' clause 

    return Data.F[a]
#end procedure Traverse()


def iamlate(T, V, q, length):
    #
    T.append(length)
    Data = CreateData(T, V, q, length)
    value = Traverse(Data, 0, 0)

    print( Data.parent )
    return restoreStations(Data)

#end procedure iamlate()


# runtests( iamlate )

T =  [0, 1, 2]
V =  [2, 1, 5]
q =  1
l =  4
print( iamlate(T, V, q, l) )