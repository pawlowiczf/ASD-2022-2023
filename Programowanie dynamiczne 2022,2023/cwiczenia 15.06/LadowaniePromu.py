# Dana jest tablica A[n] z długosciami samochodów, które stoja w kolejce,
# zeby wjechac na prom. Prom ma dwa pasy (lewy i prawy), oba długosci L. Prosze napisac program, który
# wyznacza, które samochody powinny pojechac na który pas, zeby na promie zmiesciło sie jak najwiecej aut.
# Auta musza wjezdzac w takiej kolejnosci, w jakiej sa podane w tablicy A.

# F(g, d, i) = True - jesli da sie rozmiescic 'i' pierwszych samochodow, tak aby na lewym pasie zajmowaly 'g' dlugosci,
# a na prawym 'd' dlugosci

# F(g, d, i) = False, jesli takie rozmieszczenie nie istnieje 

# Te funkcje mozna zredukowac do dwoch zmiennych tj. F(g, i), gdyz znajac 'g' i 'i', wiemy tez jaka jest dlugosc na prawym pasie.


def Rek(T, F, g, d, L, i):
    #
    if g < 0 or d < 0: return False 

    if i == 0: 
        if g < T[0]: return True 
        if d < T[0]: return True 
        return False 

    if (g, d, i) not in F:
        #
        flag = Rek(T, F, g - T[i], d, L, i - 1) | Rek(T, F, g, d - T[i], L, i - 1)
        F[ (g, d, i) ] = flag 
    #

    return F[ (g, d, i) ]
#end procedure 


def Prom(T, L):
    #
    n = len(T)
    F = {}

    for car in reversed( range(n) ):
        if Rek(T, F, L, L, L, car):
            return car 
    #end 'for' loop

    return -1
#end procedure Prom()