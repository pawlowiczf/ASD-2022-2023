#Ten algorytm zatrzyma się w przypadkowym miejscu, gdy odnajdzie szukana wartosc
def binary_search(tab, value):

    _start = 0
    _end = len( tab ) - 1

    while _start <= _end : 

        middle = ( _start + _end ) // 2

        if value == tab[ middle ]: return middle 
        elif value < tab[ middle ]: _end = middle - 1
        else: _start = middle + 1 # elif value > tab[ middle ]

    #end while
    return -1 
#end def


# Ten algorytm zatrzyma sie na poczatku sublisty zawieracej nasze elementy, jezeli te wystepuja wielokrotnie
# np. w liscie [1,2,3,3,3,3,4,5] zmienna _start bedzie przechowywac indeks 2 
# algorytm można zmienic, aby wskazywal na ostatnia szukana wartosc (tj. indeks 5, zmienna _start takze to przechowuje) 
# zmiekczajac nierownsoc w petli while w linijce 34

def binary_search2(tab, value):
    
    _start = 0
    _end = len( tab ) - 1

    while _start <= _end:
        
        middle = ( _start + _end ) // 2

        if value > tab[ middle ]: _start = middle + 1
        else: _end = middle - 1
    #end while

    if _start < len(tab) and tab[ _start ] == value: return _start
    return -1

# ---------------------------

# Przeksztalcenie funkcji binary_search (funkcji pierwszej) do postaci rekurencyjnej:
def binary_search_rek(tab, value, _start, _end):

    if _start > _end:
        return -1
    
    middle = ( _start + _end ) // 2

    if tab[ middle ] == value: return middle 
    if tab[ middle ] < value: return binary_search_rek(tab, value, _start, middle -1)
    return binary_search_rek(tab, value, middle + 1, _end)
#end def

T = [1,2,3,3,3,3,3,4,5,6,7]
print( binary_search( T , 3) )
print( binary_search2( T , 3) )
print( binary_search_rek(T, 3, 0, len(T) - 1 ) )
