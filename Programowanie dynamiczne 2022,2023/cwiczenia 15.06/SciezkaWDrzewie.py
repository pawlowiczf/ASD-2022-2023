# Dane jest drzewo ukorzenione T, gdzie kazdy wierzchołek v ma—
# potencjalnie ujemna—wartosc value(v). Prosze zaproponowac algorytm, który znajduje wartosc najbardziej
# wartosciowej sciezki w drzewie T.

# 2 rozwiazanie: drzewo binarne i dowolne 


# Dla drzewa binarnego:

class Node:
    def __init__(self, value, right = None, left = None):
        self.value = value 
        self.left  = left 
        self.right = right
#end class

def MaxPath(root):
    #
    bestValue = -float('inf')

    def Rek(a):
        #   
        nonlocal bestValue
        if a == None: return 0

        leftMax = Rek( a.left )
        rightMax = Rek( a.right )
        bestValue = max( bestValue, a.value + leftMax + rightMax)

        currValue = max(0, a.value + max( leftMax, rightMax ) )
        return currValue 
    #end procedure Rek()
    
    Rek(root)
    return bestValue
#end procedure MaxPath()



v = Node(5)
u = Node(-2)
w = Node(3)
z = Node(10)
v.left = u
v.right = w
w.left = z
print( MaxPath(v) ) # 18 


root = Node(-4, 
            Node(10,
                Node(7,
                    Node(8,
                        Node(1,
                            Node(-5,
                                Node(-4)
                            )
                        ),
                        Node(-7, 
                            right=Node(1)
                            )
                    )
                ),
                Node(-5,
                     Node(-100),
                     Node(2,
                          Node(20),
                          Node(7)
                         )
                    )
                ),
            Node(-8)
            )

print(MaxPath(root)) # 43 



# Dla dowolnego drzewa:


class Node:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
#end def

def Update(maxPaths, maxChildren):
    #
    if maxPaths[0] > maxPaths[1] and maxChildren > maxPaths[1]:
        maxPaths[1] = maxChildren

    elif maxChildren > maxPaths[0]:
        maxPaths[0] = maxChildren 
#end procedure Update()

def MaxPathTree(root):
    #
    bestValue = -float('inf')

    def Rek(a):
        #
        nonlocal bestValue 
        maxPaths = [0, 0]

        for child in a.children:
            value = Rek(child)
            Update(maxPaths, value)
        #

        bestValue = max( bestValue, a.value + sum(maxPaths) )

        currValue = max(0, a.value + max( maxPaths ) )  
        return currValue 
    #end procedure Rek()
    
    Rek(root)
    return bestValue
#end procedure MaxPathTree()

root = Node(20, [
    Node(5, [
        Node(30), 
        Node(-20)
    ]), 
    Node(-20, [
        Node(1, [
            Node(30), 
            Node(22),
            Node(-15)
        ]), 
    ]), 
    Node(15),
    Node(-10, [
        Node(18),
        Node(23),
        Node(-20, [
            Node(100)
        ]),
        Node(-15)
    ])
])

print( MaxPathTree(root) )