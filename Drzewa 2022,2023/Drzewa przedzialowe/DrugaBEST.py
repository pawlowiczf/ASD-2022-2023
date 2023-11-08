def removeRepetitions(keys):
    #
    keys.sort()
    length = len(keys)
    newArray = [] 

    for a in range( length - 1 ):
        if keys[a + 1] != keys[a]:
            newArray.append( keys[a] )
    #

    newArray.append( keys[length - 1] )
    return newArray
#end procedure removeRepetitions()

class Node:
    def __init__(self):
        self.key    = None    # klucz tego wezla
        self.leftspan   = None    # span = [self.left, self.right]
        self.rightspan  = None
        self.intervals = []   # przedzialy zgromadzone w tym wezle
        self.left   = None    # lewe dziecko
        self.right  = None    # prawe dziecko
        self.leaf   = False   # czy to lisc?
#end class 

def constructTree(keys, low, high, leftspan, rightspan):
    #
    node = Node()
    node.leftspan  = leftspan 
    node.rightspan = rightspan 

    if low > high: # this is leaf 
        node.leaf = True 
        node.key  = "Leaf"
    
    else:
        middle = ( low + high ) // 2 
        node.key = keys[ middle ]

        node.left  = constructTree( keys, low, middle - 1, leftspan, keys[ middle ] )
        node.right = constructTree( keys, middle + 1, high, keys[ middle ], rightspan )

    #end 'if' clause

    return node 
#end procedure constructTree()

# (a, b) - interval
def insertInterval(T, a, b):
    #

    # if span(T) is a part of interval:
    if a <= T.leftspan <= T.rightspan <= b:
        T.intervals.append( (a, b) )
        return
    
    else:
        if a < T.key: 
            insertInterval(T.left, a, b)
        if T.key < b: 
            insertInterval(T.right, a, b)
    
    #end 'if' clause 
#end procedure insertInterval()

def removeInterval(T, a, b):
    #
    if a <= T.leftspan <= T.rightspan <= b:
        if (a, b) in T.intervals: T.intervals.remove( (a, b) )
        return 
    else:
        if a < T.key: 
            insertInterval(T.left, a, b)
        if T.key < b: 
            insertInterval(T.right, a, b)

    #end 'if' clause
#end procedure removeInterval()

def createIntervalTree(listIntervals):
    #  keys - tablica posortowana rosnaco, bez powtorzen, z kluczami (wartosci brzegowe przedzialow)
    keys = []

    for (a, b) in listIntervals:
        keys.append(a)
        keys.append(b)
    #

    keys = removeRepetitions(keys)
    T    = constructTree( keys, 0, len(keys) - 1, -float('inf'), float('inf') )

    for (a, b) in listIntervals:
        insertInterval(T, a, b)
    #
    return T
#end procedure createIntervalTree()

def containingValue(T, value):
    #
    if T.Leaf: return T.intervals 
    
    array = []
    array += T.intervals 

    if value <= T.key: array += containingValue(T.left, value)
    if value >= T.key: array += containingValue(T.right, value)

    return array 
#end procedure containingValue()


# -------------------------------------------------

def tree_print(X, ind=""):

    if X.leaf:
        print(ind, "leaf-span: [%f, %f] --> " % (X.leftspan, X.rightspan), X.intervals)
    if not X.leaf:
        print(ind, "cut = %d," % X.key, "span = [%f, %f], " % (X.leftspan, X.rightspan), "intervals =", X.intervals)
        tree_print(X.left, ind + "  ")
        tree_print(X.right, ind + "  ")
#end procedure tree_print

P = [ [0, 10], [5, 20], [7, 12], [10, 15] ]
T = createIntervalTree(P)
tree_print(T)

