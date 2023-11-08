# kol2test_spec.py
from math import sqrt

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

Ge =  [ [(1,3), (2,1), (4,2)],
      [(0,3), (2,5) ],
      [(1,5), (0,1), (3,6)],
      [(2,6), (4,4) ],
      [(3,4), (0,2) ] ]

Ge2 = [ [(1,2), (2,3)], # 0
        [(0,2), (2,1), (3,5), (4,6)], # 1
        [(0,3), (1,1), (3,9), (4,4)], # 2
        [(1,5), (2,9), (4,10), (5,8)], # 3
        [(2,4), (1,6), (3,10), (5,7)], # 4
        [(3,8), (4,7)] ] # 5



TEST_SPEC = [
  # n m has_tree p hint
  # n - liczba wierzcholkow (<10 oznacza bezpośrednie wejście)
  # m - liczba krawedzi
  # has_tree - czy ma piekne drzewo
  # p - prawdopodobieństwo przyjecia wezla do drzewa
  # hint - rozwiazanie
  (0, Ge, -1, -1, 10 ),
  (1, Ge2, -1, -1, 25 ),
  (5, 10, True, 0.5, 1865),
  (10, 30, True, 0.5, 41549),
  (20, 150, True, 0.5, 865632),
  (20, 350, True, 0.5, 832477),
  (50, 1000, True, 0.25, 31864990),
  (100, 10000, True, 0.125, 531518800),
  (1000, 25000, True, 0.125, 2208192932987),
  (2000, 25000, True, 0.0825, 4403207041036),
  (500, 12500, False, 0.0825, None),
  (700, 18500, False, 0.0825, None),
]


from testy import MY_random

def my_randint(a,b):
  return a+MY_random()%(b-a+1)


def splitlist( A, p ):
  R = []
  L = []
  for x in A:
    if my_randint(1,100)/100 <= p:
      R.append(x)
    else:
      L.append(x)
  return R,L

def split( A, p ):
  LISTS = []
  while True:
    R,A = splitlist( A, p )
    LISTS.append( R )
    if len(A) <= len(R):
      LISTS.append(A)
      return LISTS

def buildtree( n, p, weights ):

  edges = set()

  def getweight( ):
    nonlocal weights
    return weights.pop()

  def btree( root, nodes ):
    nonlocal G, p, edges
    ch = split( nodes, p )
    for children in ch:
      if len(children) == 0: continue
      rt = children[0]
      children = children[1:]
      w = getweight()
      G[root].append( (rt, w) )
      G[rt].append( (root, w) )
      edges.add( (rt, root) )
      edges.add( (root, rt) )
      btree( rt, children ) 
      
    
  
  G = [[] for i in range(n)]
  V = list(range(n))
  root = V[0]
  V = V[1:]
  btree( root, V)

  return G, edges



def genedges( G, n, E, to_gen, minW, maxW ):
    W = [my_randint( minW, maxW ) for i in range(to_gen)]
    W.sort()
    for i in range(1,len(W)):
      if W[i] <= W[i-1]: W[i] = W[i-1]+1

    for i in range( to_gen ):
      u = my_randint( 0, n-1 )
      v = my_randint( 0, n-1 )
      if u == v: continue
      if (u,v) in E: continue
      E.add((u,v))
      E.add((v,u))
      ww = W.pop()
      G[u].append((v,ww))
      G[v].append((u,ww))



def gentest(n, edges, has_tree, p , hint ):
  if n < 5:
    G = edges
    return [G],hint

  if has_tree:
    m = 10*n*n
    M = 10*n*n*n
    W = [my_randint( m, M ) for i in range(n-1)]
    W.sort()
    for i in range(1,len(W)):
      if W[i] <= W[i-1]: W[i] = W[i-1]+1

    G, E = buildtree( n, p, W )

    p1 = my_randint(1,100)/100
    edges -= n-1
    e1 = int(edges * p1)
    e2 = edges - e1


    genedges( G, n, E, e1, 1, m-1 )
    genedges( G, n, E, e2, M+1, 3*M )
#    print(f"{e1}/{e2}")
  else:
    G = [ [] for i in range(n) ]
    genedges( G, n, set(), edges, 1, (10*n*n*n) )

  for i in range(n):
    G[i].sort()

#  for i in range(n):
#    print(f"G[{i}]:  {G[i]}" )
#  print("generated ^^^")


  return [G],hint
   

  
