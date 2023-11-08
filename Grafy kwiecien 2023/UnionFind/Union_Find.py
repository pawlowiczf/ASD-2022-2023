class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0
    #
#end Class

def Find(x):
    if x.parent != x:
        x.parent = Find( x.parent )
    #
    return x.parent
#end procedure Find()


def Union(X, Y):
    #
    X = Find(X)
    Y = Find(Y)
    #
    if X.rank > Y.rank:
        Y.parent = X

    elif X.rank < Y.rank:
        X.parent = Y

    else:
        X.parent = Y 
        Y.rank += 1
#end procedure Union()


    
