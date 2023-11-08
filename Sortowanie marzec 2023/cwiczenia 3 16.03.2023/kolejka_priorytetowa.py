# Kolejka priorytetowa

def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1) // 2

def heapify(T,i,n):
    l = left(i)
    r = right(i)

    max_ind = i
    if l < n and T[ l ] > T[ max_ind ]: max_ind = l
    if r< n and T[ r ] > T[ max_ind ] : max_ind = r 

    if max_ind != i:
        T[i], T[ max_ind ] = T[ max_ind ], T[i]
        heapify(T, max_ind, n)
#end def ^^^

def buildheap(T):
    n = len(T)
    for i in range( parent( n - 1), -1, -1):
        heapify(T, i, n)
#end def ^^^


def shift_up(i):
    while i > 0 and T[ parent(i) ] < T[ i ]:
        T[ parent(i) ], T[i] = T[i], T[ parent(i) ]
        i = parent(i)
#end def ^^^


def print_queue(T):
    global size
    i = 0
    while i <= size:
        print(T[i], end = " ")
        i += 1
#end def ^^^


def extract_max(T):
    #
    global size
    max_element = T[0]
    T[0] = T[size]
    size -= 1
    #
    heapify(T, 0, size)
    #
    return max_element
#end def ^^^


def insert_key(key):
    global size
    k = len(T) - 1
    #
    if size == k: 
        print("Brak miejsca")
        return 0
    #
    size = size + 1
    T[size] = key 
    shift_up(size)
    #end while

#end def ^^^



size = -1
T = [0]*50


insert_key(45)
insert_key(20)
insert_key(14)
insert_key(12)
insert_key(31)
insert_key(7)
insert_key(11)
insert_key(13)
insert_key(7)


print_queue(T)



