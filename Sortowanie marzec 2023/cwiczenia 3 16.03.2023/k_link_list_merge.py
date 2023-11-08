# Nie jestem pewien, czy dobrze, niby dziala, ale nie rozumiem.
# Lepsze rozwiazanie znajduje sie w folderze 500

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


# Mamy k posortowanych link-list. Scal je w jedna posortowana.
# Wykorzystujemy kopiec min, w kopcu sa glowy list 

def parent(i): return (i-1) // 2
def right(i): return 2*i + 2
def left(i): return 2*i + 1

def heapify(T,i,n): # naprawia drzewo, jesli w korzeniu znajduje sie zla wartosc
    l = left(i)
    r = right(i)
    min_ind = i

    if l < n and T[l].val < T[min_ind].val: min_ind = l
    if r < n and T[r].val < T[min_ind].val: min_ind = r

    if min_ind != i:
        T[min_ind], T[i] = T[i], T[min_ind]
        heapify(T, min_ind,n)
#end def 



# def insert(T, element):
#     T.append( element )
#     n = len(T) - 1
#     #
#     while n > 0 and T[ parent(n) ].val > T[n].val:
#         k = parent(n)
#         T[k], T[n] = T[n], T[k]
#         n = k
#     #end while
# #end def ^^^


def extractMin(T):
    n = len(T) - 1
    #
    min_element = T[0]
    T[0], T[n] = T[n], T[0]
    T.pop( n )
    heapify(T, 0, n)
    return min_element
#end def ^^^

def build_heap(L):
    n = len(L)
    for i in range( parent(n-1) , -1, -1 ):
        heapify(L, i, n)

#end def ^^^

def merge(H):
    build_heap(H)
    a = Node(None)
    last = a
    #
    while H:
        last.next = H[0]
        H[0] = H[0].next
        last = last.next
        H[0], H[ len(H) - 1 ] = H[ len(H) - 1 ], H[0]
        #
        if H[ len(H) - 1 ] is None:
            H.pop( len(H) - 1 )
        heapify( H, 0, len(H) )
    #end while
    return a.next
#end def 


p = create_link_list( [1,1,5,8,10,15,19,23,25,29,34] )
q = create_link_list( [-10,1,3,5,16,19,34] )
k = create_link_list( [-5,6,19,20] )
L = [p,q,k]
a = merge(L)
print_linklist(a)
