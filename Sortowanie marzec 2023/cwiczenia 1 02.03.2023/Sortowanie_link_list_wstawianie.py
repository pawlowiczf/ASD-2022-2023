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


# Sortowanie link-listy przez wstawianie

def insert(pointer, node):
    head = pointer

    # Jesli jeszcze nie dodano zadnego element do nowo-tworzonej listy
    if pointer is None:
        return node 
    
    # Jesli element trzeba wstawic na poczatek:
    if node.val <= pointer.val:
        node.next = pointer
        return node
    #
    while pointer.next is not None:
        if pointer.val <= node.val and node.val <= pointer.next.val:
            node.next = pointer.next
            pointer.next = node
            return head
        pointer = pointer.next 
    #end while
    pointer.next = node
    return head
#end def 


def sortowanie(pointer):
    new_pointer = None
    #
    while pointer is not None:
        head = pointer
        pointer = pointer.next
        head.next = None
        new_pointer = insert(new_pointer, head)
    #end 
    return new_pointer
#end def 
        


T = [-10,15,3,-11,1,8,5,156,-600,41,8,-150,5,6]
p = create_link_list(T)
print_linklist(p)
print()
new_pointer = sortowanie(p)
print_linklist(new_pointer)



    