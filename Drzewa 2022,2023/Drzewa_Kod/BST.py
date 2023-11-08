
class BST:
    def __init__(self, key, parent = None, left = None, right = None):
        self.left   = left
        self.right  = right 
        self.parent = parent
        self.key    = key 
        # self.data = data 

#end class


# Operacje na drzewie BST:
# search, insert, remove, min / max, parent, poprzednik-nastepnik, print in order
# -----------------------------------------------------------------------------------

def printOrder(x):
    #
    if x is None: return 

    printOrder(x.left)
    print(x.key, end = ' ')
    printOrder(x.right)
#end procedure printOrder()

def Search(key, x):
    #
    while x != None:
        #
        if x.key == key: return x 

        if x.key < key:
            x = x.right 
        else:
            x = x.left 

    #end 'while' loop 

    return None 
#end procedure Search()

def Insert(key, x):
    #
    if x == None: 
        x = BST(key)
        return x 

    pointer = x 
    while x != None:
        parent = x 
        if x.key < key: x = x.right 
        else: x = x.left 
    #end 'while' loop

    x = BST(key)
    x.parent = parent 

    if key < parent.key:
        parent.left = x 
    else:
        parent.right = x 
    #

    return pointer 
#end procedure Insert()

def constructBST(keys):
    #
    root = None 

    for key in keys:
        root = Insert(key, root)
    #

    return root 
#end procedure constructBST()

def Min(x):
    #
    while x.left: 
        x = x.left 
    #
    return x.key
#end procedure Min()

def Max(x):
    # 
    while x.right:
        x = x.right 
    #
    return x.key 
#end procedure Max()

# succ(x) - jesli x ma prawe dziecko, to znajdz minimum w prawym poddrzewie x 
# jesli x nie ma prawego dziecka, to wedruj w gore drzewa, poki jestes prawym synem. 

def Successor(x, key): #nastepnik
    #
    if x is None: return x 
    succ = None 

    while x is not None:
        #
        #innymi slowy, aby znalezc nastepnik x (ktory tam nie ma prawego dziecka), to trzeba znalezc takiego node'a, że poprzednik node'a to x. 
        if key < x.key:
            succ = x 
            x = x.left 

        elif x.key < key:
            x = x.right 
        
        else:
            if x.right is not None:
                return Min( x.right )
            return succ.key
    #
    return succ.key # w sytuacji gdy x == None (x nie ma w drzewie) zwracamy najwieksza liczbe zaraz po x
    return succ 
#end procedure Successor()

def Predecessor(x, key): #poprzednik 
    #
    if x is None: return x 
    pred = None 

    while x is not None:
        #
        if key < x.key:
            x = x.left

        elif x.key < key: 
            pred = x 
            x = x.right 
        
        else:
            if x.left is not None:
                return Max( x.left )
            return pred 
    #
    return pred.key 
    return pred
#end procedure Predecessor()


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.key))
        printTree(node.left, level + 1)
#end def



keys = [15, 10, 20, 8, 12, 16]
x = constructBST(keys)

printOrder(x)
print()

# ---------

# keys = [8, 3, 10, 1, 6, 14, 4, 7, 12] 
# x = constructBST(keys)
# printOrder(x)
# print()
