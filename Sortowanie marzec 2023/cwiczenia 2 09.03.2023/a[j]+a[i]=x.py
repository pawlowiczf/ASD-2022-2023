# Mamy posortowana tablice liczb naturalnych i pytamy, czy znajduja sie w niej takie elementy, ze a[i] + a[j] = X, gdzie x > 0 i x nalezy do naturalnych

def find(T, X):
    i = 0
    j = len(T) - 1

    while i <= j:

        if T[i] + T[j] < X:
            i += 1
        elif T[i] + T[j] > X:
            j -= 1
        else:
            return True 
    #end while
    return False
#end def ^^^


T = [1,4,6,11,15,20,26,30,50,50]
# print( find(T,31) )


# To samo zadanie, ale szukamy a[i] - a[j] = X

def find2(T,X):
    i = 0
    j = 0

    while i < len(T):
        if T[i] - T[j] < X:
            i += 1
        elif T[i] - T[j] > X:
            j += 1
        else:
            return True
    #end while
    return False
#end def ^^^



T = [1,4,6,11]
# print( find2(T, 4) )