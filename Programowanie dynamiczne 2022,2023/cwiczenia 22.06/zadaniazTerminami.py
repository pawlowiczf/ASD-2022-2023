# Mamy dany zbiór zadan T = {t1, . . . , tn}. Kazde zadanie ti
# dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie w
# terminie (liczba naturalna). 

# Wykonanie kazdego zadania trwa jednostke czasu. Jesli zadanie ti zostanie
# wykonane przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrode g(ti) (pierwsze wybrane
# zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
# Prosze podac algorytm, który znajduje podzbiór zadan, które mozna wykonac w terminie i który prowadzi
# do maksymalnego zysku. Prosze uzasadnic poprawnosc algorytmu.


def TaskSequencing(T):
    #
    T.sort( key = lambda x: x[1], reverse = True )
    size = 0

    for (deadline, profit) in T:
        size = max(size, deadline)
    #

    slots  = [ False for _ in range(size + 1) ] 
    result = []

    for (deadline, profit) in T:
        #
        for place in reversed( range(deadline) ):

            if not slots[place]:
                slots[place] = True 
                result.append( (deadline, profit) )
                break
            #

        #end 'for' loop 

    #end 'for' loop

    return result 
#end procedure TaskSequencing()

A = [[2, 50],
     [1, 21],
     [2, 27],
     [3, 25],
     [2, 15]
]
print( TaskSequencing(A) )


A = [[2, 100],  
     [1, 19],
     [2, 27],
     [1, 25],
     [3, 15] ]
print( TaskSequencing(A) )
print( " ------------------------- ")

# Drugie rozwiazanie z uzyciem Disjoint-Set Structures 

class Node:
    def __init__(self, id):
        self.id     = id 
        self.parent = self 
#end class Node 

def Find(x):
    #
    if x.parent == x: return x.parent 
    x.parent = Find( x.parent )
    return x.parent
#end procedure Find()

def Union(X, Y):
    #
    Y.parent = X
#end procedure Union()


def JobSequencing(T):
    #
    size = -1 
    T.sort( key = lambda x: x[1], reverse = True )
    
    for (deadline, profit) in T:
        size = max( size, deadline )
    #

    result = []
    slots  = [ Node(a) for a in range(size + 1) ]
    jobs   = [ False for _ in range(size) ]

    for (deadline, profit) in T:
        #
        parent = Find( slots[deadline] )
        
        if parent.id != 0:
            Union( slots[ parent.id - 1 ], slots[ parent.id ] )
            result.append( (deadline, profit) ) 
        #

    #end 'for' loop
     
    return result 
#end procedure JobSequencing()


A = [[2, 50],
     [1, 21],
     [2, 27],
     [3, 25],
     [2, 15]
]
print( JobSequencing(A) )
# 50, 27, 25 

A = [[2, 100],  
     [1, 19],
     [2, 27],
     [1, 25],
     [3, 15] ]
print( JobSequencing(A) )
# 100, 27, 15 