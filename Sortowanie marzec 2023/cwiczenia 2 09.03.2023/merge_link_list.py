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


# Merge link-list

def merge_two(p,q):
    k = Node(None)
    copy_k = k
    #
    if p is None: return q
    if q is None: return p
    while p is not None and q is not None:
        if p.val < q.val:
            k.next = p
            p = p.next
            k.next.next = None
        else:
            k.next = q
            q = q.next
            k.next.next = None
        k = k.next 
    #end while

    if p is None:
        while q is not None:
            k.next = q
            q = q.next
            k.next.next = q
            k = k.next 
    else:
        while p is not None:
            k.next = p
            p = p.next
            k.next.next = p
            k = k.next 
    #end
    #end
    return copy_k.next 
#end def

def split_two(p):
    slow, fast = p, p

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next 
    #end while
    second = slow.next
    slow.next = None 
    return p, second


def merge_sort(p):
    if p.next is not None:
        x, y = split_two(p)
        #
        x = merge_sort(x)
        y = merge_sort(y)
        p = merge_two(x,y) 
    #end
    return p
#end def 

# p = create_link_list( [-100,6,19,15,100,-14,6,2137,-1000,400,420 ] )
p = create_link_list( [1, 6, 3, 2, 9, 1, 9] )
p = merge_sort(p)
print_linklist(p)







