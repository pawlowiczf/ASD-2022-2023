from kol1testy import runtests

def right(a): return 2 * a + 2 
def left(a): return 2 * a + 1
def parent(a): return (a - 1) // 2

def HeapifyMin(Heap, MinIndex, a, n):
    #
    minInd = a 
    r = right(a)
    l = left(a)
    
    if r < n and Heap[r] < Heap[minInd]: minInd = r 
    if l < n and Heap[l] < Heap[minInd]: minInd = l 

    if minInd != a:
        Heap[minInd], Heap[a] = Heap[a], Heap[minInd]
        MinIndex[minInd], MinIndex[a] = MinIndex[a], MinIndex[minInd]
        HeapifyMin(Heap, MinIndex, minInd, n)
    #
#end procedure HeapifyMin()

def HeapifyMax(Heap, MaxIndex, a, n):
    #
    maxInd = a 
    r = right(a)
    l = left(a)

    if r < n and Heap[r] > Heap[maxInd]: maxInd = r 
    if l < n and Heap[l] > Heap[maxInd]: maxInd = l 

    if maxInd != a:
        Heap[maxInd], Heap[a] = Heap[a], Heap[maxInd]
        MaxIndex[maxInd], MaxIndex[a] = MaxIndex[a], MaxIndex[maxInd]
        HeapifyMax(Heap, MaxIndex, maxInd, n)
    #
#end procedure HeapifyMin()

def moveUpMinHeap(Heap, MinIndex, index):
    #
    while index > 0 and Heap[ parent(index) ] > Heap[index]:
        Heap[index], Heap[ parent(index) ] = Heap[ parent(index) ], Heap[index] 
        MinIndex[ index ], MinIndex[ parent(index) ] = MinIndex[ parent(index) ], MinIndex[ index ] 
        index = parent(index)
    #
#end procedure moveUpMinHeap()

def moveUpMaxHeap(Heap, MaxIndex, index):
    #
    while index > 0 and Heap[ parent(index) ] > Heap[index]:
        Heap[index], Heap[ parent(index) ] = Heap[ parent(index) ], Heap[index] 
        MaxIndex[ index ], MaxIndex[ parent(index) ] = MaxIndex[ parent(index) ], MaxIndex[ index ] 
        index = parent(index)
    #
#end procedure moveUpMinHeap()

def removeMinHeap(Heap, MinIndex, index):
    #
    Heap[index], Heap[-1] = Heap[-1], Heap[index] 
    Heap.pop()

    if Heap[ parent(index) ] < Heap[index]:
        HeapifyMin( Heap, MinIndex, index, len(Heap) )
    else:
        moveUpMinHeap( Heap, MinIndex, index )
    #
#end procedure removeMinHeap()

def removeMaxHeap(Heap, MaxIndex, index):
    #
    Heap[index], Heap[-1] = Heap[-1], Heap[index] 
    Heap.pop()

    if parent(index) >= 0 and Heap[ parent(index) ] > Heap[index]:
        HeapifyMax( Heap, MaxIndex, index, len(Heap) )
    else:
        moveUpMaxHeap( Heap, MaxIndex, index )
    #
#end procedure removeMinHeap()

def buildHeapMin(Heap, MinIndex):
    #
    n = len(Heap)

    for a in range( parent(n - 1), -1, -1 ):
        HeapifyMin(Heap, MinIndex, a, n)
    #
#end procedure buildHeapMin()

def buildHeapMax(Heap, MaxIndex):
    #
    n = len(Heap)

    for a in range( parent(n - 1), -1, -1 ):
        HeapifyMax(Heap, MaxIndex, a, n)
    #
#end procedure buildHeapMax()

def extractHeapMin(HeapMin, MinIndex):
    #
    value = HeapMin[0]
    HeapMin[0], HeapMin[-1] = HeapMin[-1], HeapMin[0]
    HeapMin.pop()

    HeapifyMin( HeapMin, MinIndex, 0, len(HeapMin) )
    return value
#end procedure extractHeapMin()

def extractHeapMax(HeapMax, MaxIndex):
    #
    value = HeapMax[0]
    HeapMax[0], HeapMax[-1] = HeapMax[-1], HeapMax[0]
    HeapMax.pop()

    HeapifyMax( HeapMax, MaxIndex, 0, len(HeapMax) )
    return value
#end procedure extractHeapMax()

def insertHeapMax(HeapMax, MaxIndex, value):
    #
    HeapMax.append( value )
    a = len(HeapMax) - 1
    MaxIndex[a] = a 

    while a > 0 and HeapMax[ parent(a) ] < HeapMax[a]:
        HeapMax[ parent(a) ], HeapMax[a] = HeapMax[a], HeapMax[ parent(a) ] 
        MaxIndex[ parent(a) ], MaxIndex[a] = MaxIndex[a], MaxIndex[ parent(a) ]
        a = parent(a)
    #
#end procedure insertHeapMax()

def insertHeapMin(HeapMin, MinIndex, value):
    #
    HeapMin.append( value )
    a = len(HeapMin) - 1
    MinIndex[a] = a 

    while a > 0 and HeapMin[ parent(a) ] > HeapMin[a]:
        HeapMin[ parent(a) ], HeapMin[a] = HeapMin[a], HeapMin[ parent(a) ] 
        MinIndex[ parent(a) ], MinIndex[a] = MinIndex[a], MinIndex[ parent(a) ]
        a = parent(a)
    #
#end procedure insertHeapMin()

def ksum(T, k, p):
    #
    n = len(T)
    resultSum = 0

    helpArray = []
    for a in range(p): helpArray.append( T[a] )
    helpArray.sort()

    HeapMin = []
    HeapMax = []

    MaxIndex = [ -1 for _ in range(n) ]
    MinIndex = [ -1 for _ in range(n) ]

    for a in range(0, p - k):
        value = helpArray[a]
        MaxIndex[a] = a 
        HeapMax.append( value )
    #
    for a in range(p - k, p):
        value = helpArray[a]
        MinIndex[a] = a - ( p - k ) 
        HeapMin.append( value )
    #

    buildHeapMax(HeapMax, MaxIndex)
    buildHeapMin(HeapMin, MinIndex)

    resultSum = 0

    for a in range(n - p):
        #
        value = HeapMin[0] 
        resultSum += value 
        
        if MinIndex[a] != -1:
            removeMinHeap(HeapMin, MinIndex, a)
            insertHeapMax(HeapMax, MaxIndex, T[a + p])
            value = extractHeapMax(HeapMax, MaxIndex)
            insertHeapMin(HeapMin, MinIndex, value)
        
        elif MaxIndex[a] != -1:
            removeMaxHeap(HeapMax, MaxIndex, a)
            insertHeapMax(HeapMax, MaxIndex, T[a + p])

    #
        
    return resultSum
#end procedure ksum()


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( ksum, all_tests=False)

T =  [7, 9, 1, 5, 8, 6, 2, 12]
k =  4
p =  5
print( ksum(T, k, p) )