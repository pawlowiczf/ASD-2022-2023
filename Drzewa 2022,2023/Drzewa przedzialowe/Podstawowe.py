# Drzewo przedzialowe - struktura przechowujaca przedzialy i pozwalajaca odczytac liste przedzialow zawierajacych dany punkt 
# https://www.dgp.toronto.edu/public_user/JamesStewart/378notes/22intervals/

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
    def __init__(self, value, left = None, right = None):
        self.intervals = [] 
        self.value = value
        self.left  = None 
        self.right = None
        self.leftspan  = -float('inf')
        self.rightspan =  float('inf')
#end class


def ConstructBST(keys, low, high, root):
    #
    if low > high:
        return root
    #

    mid = (low + high) // 2
 
    root = Node( keys[mid] )

    if low - 1 >= 0: root.leftspan  = keys[low - 1] 
    else: root.leftspan = -float('inf')

    if high + 1 < len(keys): root.rightspan = keys[high + 1]
    else: root.rightspan = float('inf')

    if high - low == 0:
    #
        root.left  = Node("Leaf")
        root.left.leftspan = root.leftspan
        root.left.rightspan = root.value 

        root.right = Node("Leaf")
        root.right.leftspan = root.value
        root.right.rightspan = root.rightspan
        return root
    #

    root.left = ConstructBST(keys, low, mid - 1, root.left)
    root.right = ConstructBST(keys, mid + 1, high, root.right)
    
    return root
#end procedure Construct()

def intersection(a, b, start, end):
    if b < start or end < a: return (False, False) 
    return ( max(a, start), min(b, end) )
#end procedure intersection()

def insertInterval(T, a, b):
    #
    if a <= T.leftspan and T.rightspan <= b:
        T.intervals.append( (a, b) )
    
    else:
        if a < T.value:
            insertInterval(T.left, a, b)
        if b > T.value:
            insertInterval(T.right, a, b)
    #
#end procedure insertInterval()

def intervalsContainingKey(T, key):
    #
    if T != None:
        if T.intervals: print( T.intervals )

        if T.left != None and key < T.value:
            intervalsContainingKey(T.left, key)
        elif T.right != None:
            intervalsContainingKey(T.right, key)

    #end 'if' clause 
#end procedure intervalsContainingKey()

def createIntervalTree(listIntervals):
    #
    keys = []

    for (a, b) in listIntervals:
        keys.append(a)
        keys.append(b)
    #

    keys = removeRepetitions(keys)
    T    = ConstructBST(keys, 0, len(keys) - 1, None)

    for (a, b) in listIntervals:
        insertInterval(T, a, b)
    #
    
    return T
#end procedure createIntervalTree()

# def printSpan(T):
#     #
#     if T != None:
#         print(T.value, T.leftspan, T.rightspan)
#         print("--")
#         printSpan(T.left)
#         printSpan(T.right)
#     #
# printSpan(T)

listIntervals = [ (0,10), (5, 20), (7, 12), (10, 15) ]
T = createIntervalTree(listIntervals)

intervalsContainingKey(T, 11)
print("--")
intervalsContainingKey(T, 6)
print("--")
intervalsContainingKey(T, 100)
