"""
Dany jest prostokatny kawalek tkaniny o wymiarach X na Y, oraz lista n produktow, ktore
moga zostac wykonane z tej tkaniny. Do wytworzenia kazdego produktu 'i' potrzebny jest prostokatny kawalek
tkaniny o wymiarach a_i na b_i, a zysk ze sprzedazy tego produktu wynosi c_i. Zakladamy, ze podane wymiary i koszt
sa dodatnimi liczbami calkowitymi. Majac maszyne, ktora moze przeciac dowolny prostokatny kawalek tkaniny na dwa kawalki,
zaprojektuj algorytm, aby zwrocil maksymalny laczny zysk ze sprzedazy.
"""



def Cost(Y, X, P): # P - koszt danego fragmentu
    #
    n = len(P)
    F = [ [ -float('inf') for _ in range(X + 1) ] for _ in range(Y + 1) ]

    def rek(y, x):
        #
        if y == 0 or x == 0:
            F[y][x] = 0 
        #

        if F[y][x] == -float('inf'):
            F[y][x] = P[y][x]

            for a in range(1, y + 1):
                for b in range(1, x + 1):
                    if P[a][b]:
                        F[y][x] = max( F[y][x], rek(y - a, b) + rek(a, x - b) + rek(y - a, x - b) + P[a][b] ) 
            #end 'for' loop
        #end 'if' clause 

        return F[y][x] 
    #end procedure rek()
    return rek(Y, X)
#end procedure Cost()


P = [
    [0, 0, 0, 0, 0],
    [0, 1, 3, 2, 5],
    [0, 2, 4, 8, 9],
    [0, 10, 7, 13, 12],
    [0, 11, 6, 14, 15]
]
Y = 4
X = 4
print( Cost(Y, X, P) ) # 46

Y = 3
X = 4
print( Cost(Y, X, P) ) # 40