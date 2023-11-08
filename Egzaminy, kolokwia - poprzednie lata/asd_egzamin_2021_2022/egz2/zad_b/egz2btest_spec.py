# egz1atest_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n  g1, g2 hint
  (10, 10, 10, 5),
  (10, 100, 10, 11),
  (100, 100, 10, 208),
  (500, 100, 10, 1130),
  (2500, 100, 10, 5597),
  (5000, 50, 50, 12404),
  (10000, 800, 10, 21922),
  (10000, 1100, 1000, 24914),
  (10000, 500, 300, -1),
]


from testy import MY_random

def my_randint(a,b):
    return a+MY_random()%(b-a+1)

def gentest(n, g1, g2, hint):
    C = [ [ 0, [0,-1],[0,-1],[0,-1]] for i in range(n) ]
    
    for i in range(n):
      g = g1
      if MY_random() % 2 == 0:
        g = g2
        
      chest = my_randint( 1, g )
      C[i][0] = chest
      for j in range(1,4):
        diff = -2*chest
        while chest+diff < 0:
          diff = my_randint(0,20)-15          
        
        C[i][j][0] = chest + diff
        if j == 1: C[i][j][1] = i+1
        else:      C[i][j][1] = i+1+my_randint(0,8)
        if C[i][j][1] > n: C[i][j][1] = i+1
        if C[i][j][1] == n: C[i][j][1] = -1
    
    return [C], hint

