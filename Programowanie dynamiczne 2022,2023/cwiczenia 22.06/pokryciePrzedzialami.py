# Dany jest zbiór punktów X = {x1, . . . , xn} na
# prostej. Prosze podac algorytm, który znajduje minimalna liczbe przedziałów jednostkowych domknietych,
# potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jesli X = {0.25, 0.5, 1.6} to potrzeba dwóch
# przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]). Przedzial jednostkowy: [a, a + 1]


# Idea jest prosta. Ponieważ zawsze musimy pokryć wszystkie punkty, w szczególności musimy wziąć pierwszy w kolejności punkt do pierwszego przedziału. 
# Oczywiście musimy najpierw posortować punkty niemalejąco. Następnie, wystarczy, że za początek pierwszego przedziału jednostkowego, 
# przyjmiemy współrzędną pierwszego punktu, a następnie "włączymy" do niego wszystkie punkty, które leżą w odległości od początku układu współrzędnych (punktu 0) 
# nie dalszej niż odległość początku przedziału powiększona o 1. 
# Jeżeli natrafimy na punkt, który znajduje się dalej, zwiększamy licznik potrzebnych do użycia przedziałów i zapisujemy początek nwoego przedziału.


def Points(X):
    #
    n = len(X)
    X.sort()

    begin = 0
    count = 1 

    for a in range(1, n):
        #
        if X[begin] <= X[a] <= X[begin] + 1:
            continue 
        
        else:
            begin = a 
            count += 1

    #end 'for' loop

    return count 
#end procedure Points()

X = [-.5, 0, .25, .5, 1.6, 1.8, 2.6]
print( Points(X)) # 2

X = [-.51, -.5, 0, .25, .5, 1.6, 1.8, 2.6]
print( Points(X)) # 3 

X = [-.51, -.5, 0, .25, .5, 1.5, 1.8, 2.6, 2.61]
print( Points(X)) # 3