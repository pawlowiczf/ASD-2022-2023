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


# Sortowanie link-listy 

# Sortowanie przez wybieranie: trzeba napisac funkcje, ktora zwraca Node'a z najwiekszym lub najmniejszym node.value

def give_max(pointer):
    head = pointer
    tail = None
    max_node = pointer
    
    # if pointer.next is None: return pointer
    # if pointer is None: return None
    
    while pointer.next is not None:
        if pointer.next.val >= max_node.val: 
            max_node = pointer.next
            tail = pointer
        #end if
        pointer = pointer.next  
    #end while
    tail.next = max_node.next


    if tail is None:
        head = max_node.next
    else:
        tail.next = max_node.next
    #
    return max_node, head

#end def 


def sortowanie(pointer):
    new_pointer = None
    head = pointer

    while head is not None:
        x, head = give_max(head)
        x.next = new_pointer
        new_pointer = x 
    #end while
    return new_pointer
#end def 



T = [2000,1000,-10,1700,19139,13,-13,66,-19,-10,7,5,3,100,-184,600,0,-3000,-666]
# T = [-1,-5,-10]
x = create_link_list(T)
print_linklist(x)
print()
x = sortowanie(x)
print_linklist(x)
