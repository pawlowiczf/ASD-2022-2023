
class Employee:
    def __init__(self, fun, emp = []):
        self.fun = fun
        self.emp = emp # lista dzieci danego wezla
        self.f   = -1
        self.g   = -1
    #end def
    
#end class


"""
1. Okreslenie funkcji, ktore bedziemy obliczac:
- funkcja f(v), gdzie v - wezel drzewa, to wartosc najlepszej imprezy w poddrzewie zakorzenionym w 'v',
- funkcja g(v), gdzie v - wezel drzewa, to wartosc najlepszej imprezy w poddrzewie zakorzenionym w 'v', o ile 'v' nie idzie na impreze 

2. Zapis rekurencyjny:
f(v) = max( v.fun + suma E g(u): dla kazdego dziecka u wezla v, g(v) ) 
g(v) = suma E f(u): u - dziecko v 

3. Implementacja:

"""

def f(v):
    #
    if v.f >= 0: return v.f 

    x = v.fun 
    for children in v.emp:
        x += g(children)
    #
    y = g(v)

    v.f = max(x, y)
    return v.f

#end procedure f()
    

def g(v):
    #
    if v.g >= 0: return v.g

    x = 0
    for children in v.emp:
        x += f(children)
    #

    v.g = x 
    return v.g

#end procedure f()


# Testy:

root = Employee(7, [Employee(3, [Employee(13), Employee(17)]), Employee(5, [Employee(19)]), Employee(11, [Employee(23), Employee(29)] )])
f(root)
print( root.f ) #  108



root = Employee(7, [Employee(3, [Employee(13), Employee(17)]), Employee(5, [Employee(19)] ), Employee(100, [Employee(23), Employee(29)])])
f(root)
print(f(root)) # 149
