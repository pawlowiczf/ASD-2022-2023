from egz2btesty import runtests

# f(i, j) - minimalna suma odległości biurowców z pozycji X[0], . . . , X[i] do przydzielonych im
# działek, przy założeniu że biurowiec z pozycji X[i] ma przydzieloną działkę z pozycji Y [j]

# O(n^3)
def parking(X,Y):
  #
  n = len(X)
  m = len(Y)

  F = [ [ float('inf') for _ in range(m) ] for _ in range(n) ]

  for k in range(m):
    F[0][k] = abs(X[0] - Y[k])
  #

  for building in range(1, n):
    for k in range(m - 1):
      for parking in range(k + 1, m):

        F[building][parking] = min( F[building - 1][k] + abs( Y[parking] - X[building] ), F[building][parking])
  #
  return min( F[n - 1] )

#

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )

# Wzorcówka:
'''
from egz2btesty import runtests


def parking(X,Y):
  n, m = len(X), len(Y)

  F = [[INF] * m for _ in range(n)]

  for i in range(m):
    F[0][i] = min(abs(X[0] - Y[i]), F[0][i-1])

  
  for i in range(1, n):
    for j in range(1, m):
      F[i][j] = min(F[i][j], F[i][j-1], abs(X[i] - Y[j]) + F[i-1][j-1])
  return min(F[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
'''