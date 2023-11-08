# zad4test_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n - liczba wierzcholkow
# l - dlugosc oczekiwanej najkrotszej sciezki
# k - liczba najkrotszych sciezek
# r - liczba losowych krawedzi
#  n   l   k   p  hint
  [1,  0,  0,  0, []],         # 0
  [2,  0,  0,  0, []],         # 1
  [3,  0,  0,  0, []],         # 2
  [20, 6,  1,  30, [(0, 9), (9, 10), (10, 19)]],        # 3
  [100, 20,  1,  2000, [(0, 5), (5, 99)]],    # 4
  [100, 20,  2,  1000, []],    # 5
  [1000, 500,  1,  90000, [(0, 163), (163, 999)]], # 6
  [1000, 100,  1,  10000, [(0, 481), (479, 481)]], # 7
  [5000, 1000,  1,  5000, [(0, 3419), (3419, 3800), (2515, 3800), (2515, 3533), (1226, 3533), (420, 1226), (215, 420), (215, 4420), (356, 4420), (356, 4999)]], # 8
  [100000, 10000,  2,  0, [(14504, 70181), (6021, 70181), (6021, 37479), (37479, 39165), (34501, 39165), (34501, 68444), (36618, 68444), (36618, 99999)]], # 9
  [100000, 10000,  5,  0, [(6237, 40171), (6237, 99999)]], # 10
 ]


def gentest(n, l, k, r, hint ):
    from testy import MY_random

    if( n == 1 ):
      G1 = [ [1, 2], 
         [0, 2],
         [0, 1] ] 
      s1 = 0
      t1 = 2
      r1 = (0,2)
      return [G1,s1,t1], [r1]
    elif( n == 2 ):
      G2 = [ [1,4],  # 0
       [0,2],  # 1
       [1,3],  # 2
       [2,5],  # 3
       [0,5],  # 4
       [4,3]]  # 5

      s2 = 0
      t2 = 2
      r2 = [(0,1),(1,2)]
      return [G2,s2,t2], r2
    elif( n == 3 ):
      G3 = [ [1,2], #0
       [0,3], #1
       [0,4], #2
       [1,5,6], #3
       [2,7], #4
       [3,8], #5
       [3,8], #6
       [4,8], #7
       [5,6,7,9], #8    
       [8,10,11], #9
       [9,12], # 10
       [9,12], # 11
       [10,11]] #12       
      s3 = 0
      t3 = 12
      r3 = (8,9)
      return [G3,s3,t3], [r3]
    else:
      G = [ set() for i in range(n) ]
      
      #generuj losowe krawedzie
      for i in range(r):
        u = MY_random() % n
        v = MY_random() % n
        G[u].add(v)
        G[v].add(u)
        
      for _ in range(k):
        u = 0
        for __ in range(l-1):
          v = MY_random() % (n-1)
          G[u].add(v)
          G[v].add(u)
          u = v
        v = n-1
        G[u].add(v)
        G[v].add(u)
        
      GG = [ list(G[i]) for i in range(n) ]
      return [GG, 0, n-1], hint
    
      exit()
