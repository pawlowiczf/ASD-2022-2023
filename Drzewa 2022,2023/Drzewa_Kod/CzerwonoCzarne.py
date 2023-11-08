class Node: 
    def __init__(self, key):
        self.key   = key 
        self.color = None 
        self.right = None 
        self.left  = None 
        self.parent = None 
#end class

# 0 - black, 1 - red 
class RedBlackTree:
    def __init__(self):
        self.nil = Node(0) 
        self.nil.color = "Black" 
        self.root = self.nil 
#end class 

def fixUpTree(T, z):
    #
    while z.parent.color == "Red":
        #
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right 

            if y.color == "Red":
                z.parent.parent.color = "Red"
                y.color = "Black"
                z.parent.color = "Black"
                z = z.parent.parent 

            else:
                if z == z.parent.right: # jesli warunek u gory nie zaszedl, to znaczy ze y musi byc czarny
                    z = z.parent 
                    z = rotateLeft(T, z)
                #
                z.parent.color = "Black"
                z.parent.parent.color = "Red"
                z = rotateRight(T, z.parent.parent)

            #end 'if' clauses 
        
        else:
            y = z.parent.parent.left 

            if y.color == "Red":
                z.parent.parent.color = "Red"
                y.color = "Black"
                z.parent.color = "Black"
                z = z.parent.parent 
            
            else:
                if z == z.parent.left:
                    z = z.parent 
                    z = rotateRight(T, z)
                #
                z.parent.color = "Black"
                z.parent.parent.color = "Red"
                z = rotateLeft(T, z.parent.parent)

            #end 'if' clauses
        #end 'if' clauses
    #end 'while' loop 

    T.root.color = "Black"
    return T
#end procedure fixUpTree()      

def insertNode(T, z): # z - value 
    #
    node = Node(z) 

    y = T.nil 
    x = T.root 

    while x != T.nil: 
        #
        y = x 
        if z < x.key: x = x.left 
        else: x = x.right 
    #end 'while' loop 

    node.parent = y 

    if y == T.nil:
        T.root = node 
    elif z < y.key: 
        y.left = node 
    else:
        y.right = node 
    
    node.left = T.nil 
    node.right = T.nil 
    node.color = "Red" 

    T = fixUpTree(T, node)
    return T
#end procedure insertNode()

def rotateLeft(T, x): 
    #
    y = x.right 
    x.right = y.left 

    if y.left != T.nil:
        y.left.parent = x 
    
    #
    y.parent = x.parent 

    if x.parent == T.nil:
        T.root = y 

    elif x.parent.left == x: 
        x.parent.left = y 

    elif x.parent.right == x:
        x.parent.right = y 

    y.left = x 
    x.parent = y 
    #

    return x 
#end procedure rotateLeft()

def rotateRight(T, y):
    #
    x = y.left 
    y.left = x.right 

    if x.right != T.nil:
        x.right.parent = y 
    #
    x.parent = y.parent 

    if y.parent == T.nil:
        T.root = y 

    elif y.parent.left == y:
        y.parent.left = x 

    elif y.parent.right == y:
        y.parent.right = x 

    x.parent = y.parent 
    x.right = y 
    #

    return y 
#end procedure rotateRight()

def Transplant(T, u, v):
    #
    if u.parent == T.nil:
        T.root = v 
    
    elif u.parent.left == u:
        u.parent.left = v 
    
    else:
        u.parent.right = v 

    v.parent = u.parent 

    return T
#end procedure Transplant()

def Min(x):
    #
    while x.left != T.nil:
        x = x.left 
    #
    return x 
#end procedure Min()

def deleteFixUp(T, x):
    #
    # to do 
    pass



def removeNode(T, z):
    #
    y = z 
    yOriginalColor = y.color 

    if z.left == T.nil:
        x = z.right 
        T = Transplant(T, z, z.right)
    
    elif z.right == T.nil:
        x = z.left 
        T = Transplant(T, z, z.left)
    
    else:
        y = Min( z.right )
        yOriginalColor = y.color 
        x = y.right 

        if y.parent != z: 
            T = Transplant(T, y, y.right)
            y.right = z.right 
            y.right.parent = y 
        #

        T = Transplant(T, z, y)
        y.left = z.left 
        y.left.parent = y 
        y.color = z.color 
    
    if yOriginalColor == "Black":
        T = deleteFixUP(T, x)
    #

    return T






T = RedBlackTree()
# array = [2, 3, 4, 6, 7, 9, 11, 12, 14, 18, 19, 17, 20, 22]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

for value in array: 
    T = insertNode(T, value)

from wypisywanieDrzewa import binary_tree_string
print( binary_tree_string(T.root) )
        



