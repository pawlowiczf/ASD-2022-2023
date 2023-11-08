# Dana jest lista odsylaczowa, w ktorym wartosci val poszczegolnych wezlych zostaly wygenerowane zgodnie z rozkladem jednostajnym
# na przedziale [a,b]. Napisz algorytm, ktory sortuje taka liste.


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end def ^^^



def printLink(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next
    #
#end def ^^^


def createLinkList(T):
    p = Node(None)
    pSave = p
    #
    for i in range( len(T) ):
        k = Node( T[i] )
        p.next = k
        p = p.next
    #
    return pSave.next
#end def ^^^


def createLink(T):
    p = T[0]
    saveP = T[0]
    for i in range(1, len(T) ):
        p.next = T[i]
        p = p.next 
    #
    return saveP
#end def ^^^


def length(p):
    counter = 0
    #
    while p is not None:
        counter += 1
        p = p.next
    #
    return counter
#end def ^^^


def insertionSort(T):
    n = len(T)
    #
    for i in range(1, n):
        j = i
        while j > 0 and T[j-1].val > T[j].val:
            T[j-1], T[j] = T[j], T[j-1]
            j -= 1
        #
    #end for
    return T
#end def ^^^


def bucketSort(p, a,b):
    pSave = p
    n = length(p)
    buckets = [ [] for _ in range(n) ]
    
    for i in range(n):
        index = min( n - 1, int ( ( p.val / b ) * n ) )
        #
        temp = p
        p = p.next 
        temp.next = None 
        #
        buckets[ index ].append( temp )
    #end for
    
    for i in range(n):
        buckets[i] = insertionSort( buckets[i] )
    #end for 
    
    newList = Node(0)
    newListGuardian = newList
    for i in range(n):
        if len( buckets[i] ) != 0:
            k = createLink( buckets[i] )
            newList.next = k
            newList = buckets[i][-1]
    #
    return newListGuardian.next
#end def ^^^
        

T = [4,16,18,3,9,5,24,39,15,38,28,2,1]
p = createLinkList(T)
# printLink(p)
p = bucketSort(p, 1, 39)
printLink(p)
