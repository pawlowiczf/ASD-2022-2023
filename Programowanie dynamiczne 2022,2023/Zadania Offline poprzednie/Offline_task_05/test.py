from math import *


def dist_between_cities(c1: 'first city array', c2: 'second city array'):
    return sqrt((c2[1] - c1[1]) ** 2 + (c2[2] - c1[2]) ** 2)


def create_dist_matrix(C: 'array of cities'):
    n = len(C)
    D = [[0.] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            D[i][j] = D[j][i] = dist_between_cities(C[i], C[j])

    return D


def TSP(D: 'matrix representing weighted graph'):
    # Create a helper matrix to store #TODO - description
    n = len(D)
    F = [[float('inf')] * n for _ in range(n)]
    F[0][1] = D[0][1]

    def tspf(i, j):
        if F[i][j] == float('inf'):
            if j - i == 1:
                for k in range(i):
                    F[i][j] = min(F[i][j], tspf(k, i) + D[k][j])
            else:
                F[i][j] = tspf(i, j - 1) + D[j - 1][j]

        return F[i][j]

    min_l = float('inf')
    k = 0  # This variable will hold a pointer to the beginning of the last path segment
    for i in range(n - 2):
        curr_l = tspf(i, n - 1) + D[n - 1][i]
        if curr_l < min_l:
            min_l = curr_l
            k = i

    return min_l, k, F


def get_paths(k, F, D):
    n = len(D)
    path = [[] for _ in range(n)]
    # There will always be a segment of a resulting path which
    # connects points of index 0 and index 1, so we will store this connection
    # Similar rule applies to the last segment which was found by the TSP function
    path[0].append(1)
    path[k].append(n - 1)

    def find_paths(i, j):
        print(i, j)
        # If j == 1, then i == 0 and there are no point in looking for
        # a path as only 0 - 1 path is the remaining one.
        if j == 1:
            return
        if i < j - 1:
            print(f'adding {j - 1} -> {j}')
            path[j - 1].append(j)
            find_paths(i, j - 1)
        else:
            min_k = -1
            for k in range(i):
                if F[k][j] + D[k][j] < F[min_k][j] + D[min_k][j]:
                    min_k = k
            print('min k', min_k)
            print(f'adding {min_k} -> {j}')
            path[min_k].append(j)
            if min_k >= 0:  # TODO - check if this if statement is necessary
                find_paths(min_k, i)

    find_paths(k, n - 1)

    return path


def get_path_cycle(P: 'path array'):
    # The first point of a path will always point to two other points so
    # we can iterate over a path array twice in order to get a path from
    # both directions
    n = len(P)
    path_cycle = [0] * (n + 1)

    # Rewrite indices of subsequent cities from the first path (in the
    # first one the two directions)
    k = 1
    i = P[0][0]
    while P[i]:
        path_cycle[k] = i
        i = P[i][0]
        k += 1

    # Store an index of the last point in the path
    path_cycle[k] = i

    # Rewrite indices of subsequent cities from the second path (in the
    # second one the two directions)
    k = n - 1
    i = P[0][1]
    while P[i]:
        path_cycle[k] = i
        i = P[i][0]
        k -= 1

    return path_cycle


def get_cities_from_path(P: 'path array', C: 'array of cities'):
    print('Input path', P)
    n = len(P)
    result = [''] * n

    for i in range(n):
        result[i] = C[P[i]][0]

    return result


def bitonicTSP(C: 'array of cities'):  #TODO - getting result
    # Sort array of cities by their 'x' coordinate in an increasing order
    C.sort(key=lambda c: c[1])
    # Create a matrix of distances between cities
    D = create_dist_matrix(C)
    # Get TSP results and find the path which was calculate
    min_l, k, F = TSP(D)

    # Print subsequent cities from the calculated path

    # Return a length of the calculated path
    return min_l


C = [["Wrocław", 0, 1], ["Warszawa", 11, 5], ["Gdańsk", 4, 2],
     ["Kraków", 2, 1], ["Szczecin", 7, 3], ["Rzeszów", 0.5, 4]]
print(bitonicTSP(C))


C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
print(bitonicTSP(C))

C = [['A', 0, 2],
     ['B', 1, 1],
     ['C', 3, 2],
     ['D', 6, 0],
     ['E', 9, 0],
     ['F', 8, 5],
     ['G', 5, 5],
     ['H', 2, 4],
     ['I', 7, 0]
]
print(bitonicTSP(C))

C = [
    ['A', 0, 6],
    ['B', 1, 0],
    ['C', 6, 1],
    ['D', 8, 2],
    ['E', 7, 5],
    ['F', 5, 4],
    ['G', 2, 3]
]
print(bitonicTSP(C))

C = [["Paprykarz-Szczeciński", 1, 3], ["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]
print(bitonicTSP(C))


C = [['A', 0, 2], ['B', 1, 1], ['C', 4, 1], ['D', 5, 3], ['E', 6, 3], ['F', 8, 3], ['G', 7, 4], ['H', 2, 4],
     ['I', 0.5, 2.5], ['J', 1.5, 3.5]]
print(bitonicTSP(C))


C = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3], ["F", 0.5, -2]]
print(bitonicTSP(C))

C = [["1", 0, 1], ["2", 1, -6], ["3", 3, -1], ["4", 6, -2], ["5", 10, 1], ["6", 14, 3], ["7", 9, 4], ["8", 7, 2],
     ["9", 4, 3], ["10", 2, 3]]
print(bitonicTSP(C))



