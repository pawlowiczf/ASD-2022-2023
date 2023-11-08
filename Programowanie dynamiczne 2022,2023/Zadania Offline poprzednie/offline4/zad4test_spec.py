# zad4test_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
#  n   w   h   c  p   hint
  [1,  0,  0,  0, 0,     14],
  [5,  4,  6, 20, 40,    27],
  [10, 4,  6, 20, 20,    48],
  [10, 4,  6, 20, 20,    49],
  [100, 4,  6, 20, 20,  152],
  [100, 4,  6, 20, 20,  234],
  [100, 4,  6, 100, 200,  853],
  [100, 8,  20, 100, 400,  953],
  [100, 20,  40, 100, 500,  684],
  [50, 100,  400, 1000, 100,  2130],
]


def gentest(n, w, h, c, p, hint ):
    from testy import MY_random

    if( n == 1 ):
          T = [ (2, 1, 5, 3), 
                (3, 7, 9, 2),
                (2, 8, 11, 1) ]
          p = 5
          return [T,p], 14
    else:
      T = []
      for i in range(n):
        a = i+((MY_random() % (2*w))-w)
        if a < 1: a = 1        
        b = a + 1 + (MY_random() % w)
        h = 2 + (MY_random() % h )
        w = 1 + (MY_random() % c )
        T.append((h,a,b,w))
      return [T,p], hint