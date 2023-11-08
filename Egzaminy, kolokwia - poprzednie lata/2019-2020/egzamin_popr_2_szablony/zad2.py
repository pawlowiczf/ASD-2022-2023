from zad2testy import runtests

def HighestTower(A):
    #
    n = len(A)
    F = [1 for _ in range(n)]

    # F[i] - wysokosc najwyzszej wiezy, gdy klocek 'i' znajduje sie na samej gorze

    for a in range(1, n):
        x1, x2 = A[a]

        for b in range(a):
            y1, y2 = A[b]

            if y1 <= x1 and x2 <= y2:
                F[a] = max(F[a], F[b] + 1 )
    #

    return max(F)
#end procedure HighestTower()

def tower(A):
    #
    return HighestTower(A)


runtests(tower)
