# zad5test_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n pol, m plam roby o wartosciach od a do a+(b-1), pole numer 0 ma wartosc co najmniej c
#  n   m   a   b   c   hint
  [1,  0,  0,  0  ,0,  -1],
  [2,  0,  0,  0  ,0,  -1],
  [10, 7,  2,  3  ,3,  2],
  [50, 31,  1,  3 ,3,  13],
  [100, 31,  2,  10 ,3,  8],
  [1000, 100,  10,  30 ,3,  27],
  [10000, 100,  10,  3000 ,3,  4],
  [10000, 5000,  2,  4 ,5,  1450],
  [50000, 5000,  2,  40 ,50,  1194],
  [100000, 25000,  5,  3 ,5,  10501],
 ]


def gentest(n, m, a, b, c, hint ):
    from testy import MY_random

    if( n == 1 ):
      T = [3,0,2,1,0,2,5,0]
      return [T], 3
    elif( n == 2 ):
      T = [7,0,0,1,0,3,0,6,0,0,0,0,0,0,0,0]
      return [T],3      
    else:
      T = [0]*n
      for j in range(m):
        F = 0
        if j > 0: 
          pos = MY_random() % n
        else:
          pos = 0
          F += c
        F   += a + (MY_random() % b)
        T[pos] += F
      return [T], hint
