# zad1test_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  (3, 10, 21),
  (30, 10, 21),
  (10, 100, 197),
  (100, 100, 199),
  (100, 1000, 1981),
  (100, 1000, 1997),
  (100, 3000, 5933),
  (10, 20000, 36671),
  (10, 20000, 39229),
  (20, 20000, 34621),
]

from testy import MY_random

def my_randint(a,b):
    return a+MY_random()%(b-a+1)


def genpalindrome( m ):
  alphabet = "qwertyuiopasdfghjklzxcvbnm"
  beg = [alphabet[my_randint(0,len(alphabet)-1)] for i in range(m)]
  s = ("".join(beg)) + (alphabet[my_randint(0,len(alphabet)-1)])
  beg.reverse()
  s +=  "".join(beg)
  return s

def gentest(reps, pals, hint):
    s = ""
    for i in range(reps):
      ll = my_randint(1,pals)
      s += genpalindrome( ll )
    return [s], hint
