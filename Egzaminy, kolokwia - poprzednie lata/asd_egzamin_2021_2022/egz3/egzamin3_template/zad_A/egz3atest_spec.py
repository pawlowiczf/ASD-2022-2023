# egz3atest_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# T n hint
  (10**3, 100, 57),
  (10**3, 1000, 499),
  (10**4, 10**4, 4999),
  (10**5, 10**4, 5012),
  (10**5, 2*10**4, 10067),
  (10**8, 5*10**4, 25217),
  (10**8, 10**5, 50126),
  (10**9, 2*10**5, 100452),
  (10**9, 3*10**5, 149906)
]

from testy import MY_random

def my_randint(a,b):
    return a+MY_random()%(b-a+1)


def gentest(T, n, hint):
    I = [(my_randint(0, T-1), my_randint(0, T-1)) for _ in range(n)]
    for i in range(n):
        if I[i][0] > I[i][1]:
            I[i] = (I[i][1], I[i][0])

    return [T, I], hint
