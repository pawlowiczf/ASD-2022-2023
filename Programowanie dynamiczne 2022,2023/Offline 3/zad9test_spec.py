# zad9test_spec.py

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n, mo, mc, t, hint
  (5, 7, 10, 7, 10),
  (100, 10, 10, 10, 262),
  (100, 10, 100, 200, 8),
  (1000, 1000, 1000, 100000, 18),
  (1000, 10**4, 10**4, 10**6, 296),
  (1000, 2*10**4, 10**6, 2*10**6, 76026),
  (1000, 10**5, 10**7, 10**7, 105020),
  (2*10**4, 10, 1000, 10**4, 15),
  (2*10**4, 10, 1000, 2*10**4-1000, 8),
  (3*10**4, 10, 1000, 2*10**4, 9),
]


def gentest(n, mo, mc, t, hint):
    from testy import MY_random

    O, C = [-1]*n, [-1]*n
    last = 0
    for i in range(n):
        O[i] = last + MY_random() % mo + 1
        C[i] = MY_random() % mc + 1
        last = O[i]

    l = O[-1] + (MY_random() % mo + 1)

    for i in range(n):
        j = MY_random() % n
        tmp1, tmp2 = O[i], C[i]
        O[i], C[i] = O[j], C[j]
        O[j], C[j] = tmp1, tmp2

    return [O, C, t, l], hint

