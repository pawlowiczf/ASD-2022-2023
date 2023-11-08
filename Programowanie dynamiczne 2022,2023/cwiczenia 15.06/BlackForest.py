# Black Forest to las rosnacy na osi liczbowej gdzies w południowej Anglii. Las
# składa sie z n drzew rosnacych na pozycjach 0, . . . ,n−1. Dla kazdego i > {0, . . . ,n−1} znany jest zysk ci, jaki
# mozna osiagnac scinajac drzewo z pozycji i. John Lovenoses chce uzyskac maksymalny zysk ze scinanych
# drzew, ale prawo zabrania scinania dwóch drzew pod rzad. Prosze zaproponowac algorytm, dzieki któremu
# John znajdzie optymalny plan wycinki.

# F(i, True) - maksymalny zysk do uzyskania z wycinku drzew z przedzialu od 1 do i, pod warunkiem, że wycinamy 'i' tego drzewa
# F(i, False) - maksymalny zysk do uzyskania z wycinku drzew z przedzialu od 1 do i, pod warunkiem, że nie wycinamy 'i' tego drzewa
# F(0, ... ) = 0 (brak domow, domy z przedzialu [1, ..., n]
# F(i, True) = F(i - 1, False) + C[i]
# F(i, False) = max( F(i - 1, False), F(i - 1, True) )


def BlackForest(C):
    #
    size = len(C) 
    F = [ [ 0 for _ in range(2) ] for _ in range(size + 1) ]

    for tree in range(1, size + 1):
        #
        F[tree][1] = F[tree - 1][0] + C[tree - 1]
        F[tree][0] = max( F[tree - 1][0], F[tree - 1][1] ) 

    #end 'for' loop 

    maxRow = F[size]
    return max( maxRow )
#end procedure BlackForest


C = [1, 8, 3, 4, 5, 1, 2]
print( BlackForest(C) ) # 15 

C = [1, 8, 3, 4, 5, 2, 0, 0, 0, 0]
print( BlackForest(C) ) # 14

C = [1, 0, 8, 0, 3, 0, 4, 0, 5, 0, 2]
print( BlackForest(C) ) # 23