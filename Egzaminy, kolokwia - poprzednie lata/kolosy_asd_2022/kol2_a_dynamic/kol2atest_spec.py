# zad5test_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n punktow, z prawdopodobienstwem p jest to punkt przesiadkowy
#  n   p   hint
  [1,  0, 1],
  [2,  0, 1],
  [3,  0, 125],
  [30, 0.2, 1],
  [100, 0.1, 5],
  [100, 0.1, 7],
  [1000, 0.1, 77],
  [5000, 0.1, 408],
  [10000, 0.1, 831],
  [50000, 0.1, 3918],
 ]


def gentest(n, prob, hint ):
    from testy import MY_random

    p = True
    c = False

    if n == 1:
      #     0     1     2     3     4    5     6       7      8      9
      P = [(1,c),(3,c),(4,c),(6,c),(8,c),(9,c),(11,c),(13,c),(16,c),(17,c),
           (2,p),(5,p),(7,p),(10,p),(12,p),(14,p),(15,p),(18,p)]
      #     10    11    12    13     14     15     16     17
      B = 20        
      return [P,B], 1
    if n == 2:
      P = [(i, i%2 != 1) for i in range(1,15) ]
      return [P,15],1      
    if n == 3:
      P = [(i, i%2 != 1) for i in range(1,1000) ]
      return [P,1010],125      
    else:
      P = []
      G = 100000
      x = 1
      for i in range(n):
      
        r = ((MY_random()%G)/float(G))
        dx = 1+r*30
        x += int(dx)
        r = ((MY_random()%G)/float(G))
        if r < prob: t = True
        else: t = False
        
#        print(x,t,r,prob)
        
        P.append((x,t))
 #     exit()
      return [P,x+10],hint
    