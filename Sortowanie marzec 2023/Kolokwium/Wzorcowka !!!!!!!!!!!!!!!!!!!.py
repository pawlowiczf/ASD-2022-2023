from kol1testy import runtests

# W osobnej tablicy mamy informacje (flagi), ktore elementy naleza do kopca minimum
# W kopcach przechowujemy pary: (liczba, indeks w tablicy tej liczby)

# Jesli chcemy przesunac sie do przodu to musimy zgubic ostatni element
# Tak wlasciwie to nie musimy nic gubic. Jesli wyciagniemy element z kopca min, a bedzie on znajdowac
# sie poza zakresem, to ponownie wyciagamy z kopca min( nie psuje nam to zlozonosci, gdyz kazdy element mozemy
# wyciagnac co najwyzej 1 raz, wiec nlogn). 

# Jesli element ktory wyrzucilismy, nie byl w ogole w kopcu min ( k najwiekszych elementow ) to nadal mamy k
# najwiekszych elementow, nie liczac nowego, ktorego musimy dodac. Dodajemy nowy element do kopca max( z p - k elementami). Teraz sprawdzamy, czy 1 element z kopca min nie jest mniejszy od 1 elementu z kopca max. Jesli
# tak to zamieniamy je miejscami.

# Jesli element, ktory usuwamy byl w kopcu minimum ( z k elementow ) to przy przesuwaniu okna, to nowy element tez umieszczamy w kopcu maximum, natomiast poniewaz usunelismy jeden z elementow kopca min, to na pewno najwiekszy elemenet z kopca max, musimy przelozyc do kopca min. 

def right(a): return 2 * a + 2 
def left(a): return 2 * a + 1
def parent(a): return (a - 1) // 2

def HeapifyMin(Heap, a, n):
    #
    minInd = a 
    r = right(a)
    l = left(a)

    if r < n and Heap[r][0] < Heap[minInd][0]: minInd = r 
    if l < n and Heap[l][0] < Heap[minInd][0]: minInd = l 

    if minInd != a:
        Heap[minInd], Heap[a] = Heap[a], Heap[minInd]
        HeapifyMin(Heap, minInd, n)
    #
#end procedure HeapifyMin()

def HeapifyMax(Heap, a, n):
    #
    minInd = a 
    r = right(a)
    l = left(a)

    if r < n and Heap[r][0] > Heap[minInd][0]: minInd = r 
    if l < n and Heap[l][0] > Heap[minInd][0]: minInd = l 

    if minInd != a:
        Heap[minInd], Heap[a] = Heap[a], Heap[minInd]
        HeapifyMax(Heap, minInd, n)
    #
#end procedure HeapifyMin()

def buildHeapMin(Heap):
    #
    n = len(Heap)

    for a in range( parent(n - 1), -1, -1 ):
        HeapifyMin(Heap, a, n)
    #
#end procedure buildHeapMin()

def buildHeapMax(Heap):
    #
    n = len(Heap)

    for a in range( parent(n - 1), -1, -1 ):
        HeapifyMax(Heap, a, n)
    #
#end procedure buildHeapMax()

def extractHeapMin(HeapMin):
    #
    value, index = HeapMin[0]
    HeapMin[0], HeapMin[-1] = HeapMin[-1], HeapMin[0]
    HeapMin.pop()

    HeapifyMin(HeapMin, 0, len(HeapMin))
    return value, index
#end procedure extractHeapMin()

def extractHeapMax(HeapMax):
    #
    value, index = HeapMax[0]
    HeapMax[0], HeapMax[-1] = HeapMax[-1], HeapMax[0]
    HeapMax.pop()

    HeapifyMax(HeapMax, 0, len(HeapMax))
    return value, index
#end procedure extractHeapMax()

def insertHeapMax(HeapMax, value, index):
    #
    HeapMax.append( [value, index] )
    a = len(HeapMax) - 1

    while a > 0 and HeapMax[ parent(a) ][0] < HeapMax[a][0]:
        HeapMax[ parent(a) ], HeapMax[a] = HeapMax[a], HeapMax[ parent(a) ] 
        a = parent(a)
    #
#end procedure insertHeapMax()

def insertHeapMin(HeapMin, value, index):
    #
    HeapMin.append( [value, index] )
    a = len(HeapMin) - 1

    while a > 0 and HeapMin[ parent(a) ][0] > HeapMin[a][0]:
        HeapMin[ parent(a) ], HeapMin[a] = HeapMin[a], HeapMin[ parent(a) ] 
        a = parent(a)
    #
#end procedure insertHeapMin()

def SlidingWindows(T, k, p):
    #
    n = len(T)
    resultSum = 0

    helpArray = []
    for a in range(p): helpArray.append( [T[a], a] )
    helpArray.sort( key = lambda x: x[0] )

    HeapMin = []
    HeapMax = []

    Flag = [ False for _ in range(n) ]

    for a in range(0, p - k):
        value, index = helpArray[a]
        HeapMax.append( [value, index] )
    #
    for a in range(p - k, p):
        value, index = helpArray[a]
        Flag[index] = True
        HeapMin.append( [value, index] )
    #

    buildHeapMax(HeapMax)
    buildHeapMin(HeapMin)
    
    for a in range(n - p + 1):
        
        while HeapMin:
            value, index = HeapMin[0]
            if a <= index <= a + p - 1: break 
            Flag[index] = False
            empty, empty = extractHeapMin(HeapMin)
        #
        resultSum += value

        if Flag[a] and a + p < n: 
            insertHeapMax(HeapMax, T[a + p], a + p)
            
            while HeapMax:
                value, index = extractHeapMax(HeapMax)
                Flag[index] = False
                if a + 1 <= index <= a + p: break
            #

            insertHeapMin(HeapMin, value, index)
            Flag[index] = True 

        elif not Flag[a] and a + p < n:
            insertHeapMax(HeapMax, T[a + p], a + p)

            while HeapMax[0][0] > HeapMin[0][0]:
                index = HeapMax[0][1] 

                if a + 1 <= index <= a + p:
                    Flag[ HeapMax[0][1] ] = True 
                    Flag[ HeapMin[0][1] ] = False
                    HeapMax[0], HeapMin[0] = HeapMin[0], HeapMax[0]
                    HeapifyMax(HeapMax, 0, len(HeapMax) )
                    HeapifyMin(HeapMin, 0, len(HeapMin) )
                    break
                else:
                    empty, empty = extractHeapMax(HeapMax)

            #
        #

    #end 'for' loop 

    return resultSum
#end procedure SlidingWindows()

def ksum(T, k, p):
    #
    return SlidingWindows(T, k, p)
#end procedure ksum()


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True)


# T =  [7, 9, 1, 5, 8, 6, 2, 12]
# k =  4
# p =  5
# print( SlidingWindows(T, k, p) )


# T =  [51, 56, 45, 6, 75, 52, 49, 58, 71, 36]
# k =  2
# p =  4
# print( SlidingWindows(T, k, p) ) # 385
