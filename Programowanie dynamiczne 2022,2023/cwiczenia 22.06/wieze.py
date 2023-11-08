# Grupa m dzieci bawi sie w układanie mozliwie jak najwiekszej wiezy. Kazde dziecko
# ma klocki róznej wysokosci. Pierwsze dziecko ma klocki o wysokosciach w11,w12,w13,..., w1n,
# drugie dziecko o wysokosciach w21, w22, w23, ..., w2n itd. 
# Dzieci własnie poszły zjesc deser zanim ułoza swoje wieze, ale jedno dziecko
# zostało. Ma teraz jedyna okazje, zeby podebrac kilka klocków innym dzieciom tak, zeby jego wieza była
# najwyzsza. Prosze podac mozliwie najszybszy algorytm rozwiazujacy ten problem, który zabiera minimalna
# ilosc klocków. (Prosze zwrócic uwage, ze liczby wij moga byc bardzo duze.)

def right(a): return 2 * a + 2 
def left(a): return 2 * a + 1 
def parent(a): return ( a - 1 ) // 2

def Heapify(T, a, n):
    #
    maxInd = a
    r = right(a)
    l = left(a)

    if r < n and T[r].height > T[maxInd].height: maxInd = r 
    if l < n and T[l].height > T[maxInd].height: maxInd = l 

    if maxInd != a:
        Heapify(T, maxInd, n)
#end procedure heapify()

def BuildHeap(T):
    #
    n = len(T)

    for a in range( parent(n - 1), -1, -1 ):
        Heapify(T, a, n)
    #
#end procedure buildHeap()

def getMaximum(B, T, t):
    #
    Node = T[0] 
    index = Node.id 

    Node.height -= B[index][-1]
    value = B[index][-1]

    B[index].pop(-1)

    if Node.height < t:
        T[0], T[-1] = T[-1], T[0] 
        T.pop(-1)
    #

    Heapify( T, 0, len(T) )
    return index, value
#end procedure getMaximum()

class Height:
    def __init__(self, id, height):
        self.id = id
        self.height = height 
#end class 

def Towers(B, W, t): # B - klocki pozostalych dzieci, W - klocki naszego 'zlodzieja'
    #
    n = len(B)
    for array in B: array.sort()

    HeightTowers = [ sum( B[a] ) for a in range(n) ]
    Heap = [ Height(a, HeightTowers[a]) for a in range(n) if HeightTowers[a] >= t ]
    ourHeight = sum(W)
    BuildHeap(Heap)

    count = 0
    while Heap:
        #
        index, maxBlock = getMaximum(B, Heap, t)
        HeightTowers[index] -= maxBlock
        ourHeight += maxBlock 
        count += 1

        
    #end 'while' loop 

    valArray = []
    for array in B:
        valArray += array
    #
    valArray.sort()

    while valArray and ourHeight < t:
        ourHeight += valArray[-1]
        valArray.pop(-1)
        count += 1
    #
    return count 
#end procedure Towers()

def DriverCode(B, W):
    #
    n = len(B)
    minCount = float('inf')

    for a in range(n):
        val = 0 
        for b in B[a]:
            val += b + 1
            minCount = min( minCount, Towers(B, W, val) )
            val -= 1 
    #
    return minCount 
#end procedure DriverCode()


W1 = [4] * 8
W2 = [10]
W3 = [10, 6]
W4 = [2.75] * 6
W5 = [4, 6, 2]
others = [W1, W2, W3, W4, W5]
W0 = [2.5, 3.5]
print( DriverCode(others, W0) ) # 3


W1 = [4] * 8
others = [W1]
W0 = [2.5, 3.5]
print( DriverCode(others, W0) ) # 4


W1 = [4] * 8
W2 = [4] * 8
W3 = [4] * 8
W4 = [4] * 8
W5 = [4] * 8
W6 = [4] * 8
others = [W1, W2, W3, W4, W5, W6]
W0 = [2.5, 3.5]
print( DriverCode(others, W0) ) # 6











