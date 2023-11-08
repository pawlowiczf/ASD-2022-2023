def binary_search(T, x, left, right):
    if right - left >= 1:
        pivot = ( left + right ) // 2
        if T[ pivot ] == x: return True 
        if T[ pivot ] < x:
            return binary_search(T, x, pivot + 1, right)
        else:
            return binary_search(T, x, left, pivot - 1)
        #
    return False

#end def ^^^


