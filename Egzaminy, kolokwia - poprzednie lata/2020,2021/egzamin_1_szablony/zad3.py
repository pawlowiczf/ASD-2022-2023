from zad3testy import runtests

def Intersect(A, B):
    #
    x, y = A
    a, b = B 

    if y < a: return -float('inf'), -float('inf')
    if b < x: return -float('inf'), -float('inf')

    return [ max(x, a), min(y, b) ]
#end procedure Intersect()

def IntersectLength(A, B):
    #
    x, y = A
    a, b = B 

    if y < a: return -1
    if b < x: return -1

    return min(y, b) - max(x, a) 
#end procedure Intersect()

def restoreInterval(parent, a, k):
    #
    array = []

    while a != None:
        array.append(a)
        a = parent[a][k] 
        k -= 1
    #

    return array
#end procedure restoreInterval()

# F(i, k) - (zwraca przedzial) - przedzial, ktory jest najwiekszym przecieciem przedzialow ze zbioru [0, 1, 2, ..., i],
# wykorzystujac k przedzialow, biorac zawsze 'i'-ty przedzial

def kintersect(A, k):
    #
    n = len(A) 

    F = [ [ [-1, -1] for _ in range(k + 1) ] for _ in range(n) ]
    parent = [ [ None for _ in range(k + 1) ] for _ in range(n) ]
    for a in range(n): F[a][1] = A[a]

    for length in range(2, k + 1):
        for a in reversed( range(n) ):
            for b in range(a):
                
                array = F[b][length - 1]
                lengthOfIntersect = IntersectLength(A[a], array)

                if lengthOfIntersect != -1 and lengthOfIntersect > F[a][length][1] - F[a][length][0]:
                    parent[a][length] = b
                    F[a][length] = Intersect(A[a], array)
                #

    #end 'for' loops 

    maxLength = 0 
    vertex = -1

    for a in range(n):

        if F[a][k][1] - F[a][k][0] > maxLength:
            maxLength = F[a][k][1] - F[a][k][0]
            vertex = a 
    #
    print( maxLength )
    return restoreInterval(parent, vertex, k)
#end procedure kintersect()


runtests(kintersect)