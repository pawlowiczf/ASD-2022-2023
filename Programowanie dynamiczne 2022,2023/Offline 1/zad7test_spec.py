# egz1atest_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n  hint
(20,94),
(50,308),
(100,936),
(200,-1),
(300,2604),
(400,3470),
(500,4540),
]

from testy import MY_random

def my_randint(a,b):
    return a+MY_random()%(b-a+1)


def gentest(n, hint):
  T = [ ['.' for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if my_randint(1,10)<3: T[i][j]='#'
  T[0][0] = '.'
  T[n-1][n-1] = '.'

  L = []
  for i in range(n):
    L.append(''.join(T[i]))

  return [L],hint



