from egz2atesty import runtests

def dominance(P):
  #
  P.sort(key = lambda x: x[1])
#

  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )


''' zlozonosc O(n^2)
def dominance(P):
  #
  n = len(P)
  maxDominance = 0

  for point1 in range(n):
    dominance = 0 
    for point2 in range(n):
      a, b = P[point1]
      c, d = P[point2]
      if a > c and b > d: dominance += 1 
    #
    maxDominance = max( maxDominance, dominance)
  #

  return maxDominance
#
'''