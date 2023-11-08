# https://www.techiedelight.com/deletion-from-bst/
# Case 1: Deleting a node with no children: remove the node from the tree.
# Case 2: Deleting a node with two children: znajdz successora, zamien te wartosci ze soba i wywolaj rekurencyjnie dla wartosci successora 
# Case 3: Deleting a node with one child: remove the node and replace it with its child.

def Min(x):
    #
    while x.left: 
        x = x.left 
    #
    return x.key
#end procedure Min()

def Successor(x):
    #
    return Min( x.right )
#end procedure Successor()

def Remove(root, value):
    #
    parent = None 
    x = root 

    while x and x.key != value:
        parent = x 

        if value < x.key:
            x = x.left 
        else:
            x = x.right 

    #

    if x is None: return root # - nie znaleziono wartosci 'value' do usuniecia 

    #Case 1: no children 
    if x.left is None and x.right is None:
        #
        if x != root:
            if parent.left == x:
                parent.left = None 
            else:
                parent.right = None 
            #
        else:
            root = None 
        #
        x = None 
    #

    #Case 2: two children 
    elif x.left and x.right: #successor ma napewno jedno dziecko 
        #
        succ = Successor(x)
        Remove(x, succ)
        x.key = succ 
    #

    #Case 3: one child 
    else:
        if x.left:
            child = x.left 
        else:
            child = x.right 

        if x != root:
            if x == parent.left:
                parent.left = child 
            else:
                parent.right = child 
        else:
            root = child 
        #
        x = None 
    #

    return root 
#end procedure Remove()
            


### CORMEN DELETION ### 

def Transplant(T, u, v):
    #
    if u.parent == None:
        T = v 

    elif u == u.parent.left:
        u.parent.left = v 
    
    else:
        u.parent.right = v 
    
    if v != None: 
        v.parent = u.parent 
    
    return T 
#end procedure Transplant()

def TreeDelete(T, z):
    #
    if z.left ==  None:
        T = Transplant(T, z, z.right)
    elif z.right == None:
        T = Transplant(T, z, z.left)
    else:
        y = Successor( z.key )

        if y.parent != z:
            T = Transplant(T, y, y.right)
            y.right = z.right 
            y.right.parent = y 
        #

        T = Transplant(T, z, y)
        y.left = z.left 
        y.left.parent = y 

#end procedure TreeDelete()
        



