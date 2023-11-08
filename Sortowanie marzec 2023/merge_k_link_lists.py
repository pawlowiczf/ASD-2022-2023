class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next 
    #end def
#end class 

def create_link_list(T):
    k = Node(0)
    p = k
    for i in range(len(T)):
        x = Node( T[i] )
        k.next = x 
        k = x
    #end def
    return p.next
#end def

def print_linklist(p):
    while p is not None:
        print(p.val, end=' ')
        p = p.next
#end def


# Wykorzystam strukture kopca min


def parent(i): return (i-1) // 2
def right(i): return 2 * i + 2 
def left(i): return 2 * i + 1

def heapify(T, i, n):
    min_ind = i 
    l = left(i)
    r = right(i)
    #
    if l < n and T[l].val < T[min_ind].val: min_ind = l
    if r < n and T[r].val < T[min_ind].val: min_ind = r
    #
    if min_ind != i:
        T[i], T[min_ind] = T[min_ind], T[i]
        return heapify(T, min_ind, n)
#end def ^^^

def buildheap(T):
    n = len(T)
    for i in range( parent(n-1), -1, -1):
        heapify(T, i, n)
    #end for
#end def ^^^


def shift_up(T, pointer):
    T.append(pointer)
    i = len(T) - 1
    while i > 0 and T[ parent(i) ].val > T[ i ].val:
        T[ parent(i) ], T[i] = T[i], T[ parent(i) ]
        i = parent(i)
#end def ^^^


def extractMin(T):
    n = len(T) - 1
    #
    min_element = T[0]
    T[0], T[n] = T[n], T[0]
    T.pop(n)
    heapify(T, 0, n)
    return min_element
#end def ^^^


def merge(L):
    #
    buildheap(L)
    p = Node(None)
    guardian = p
    #
    while L:
        k = extractMin(L)
        p.next = k
        p = p.next 
        k = k.next
        #
        if k is not None:
            shift_up(L, k)
        #
    #end while
    return guardian.next
#end def ^^^


p = create_link_list( [1,5,8,10,15,19,23,25,29,34] )
q = create_link_list( [-10,3,5,16,19,34] )
k = create_link_list( [-5,6,19,20] )
L = [p,q,k]
a = merge(L)
print_linklist(a)