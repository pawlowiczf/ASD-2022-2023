# kol1test_spec.py

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  (10, 2, 4, 100, 385),
  (100, 4, 10, 1000000000, 58257747804),
  (1000, 71, 100, 1207, 326423),
  (10000, 21, 100, 942, 7311204),
  (10000, 1341, 5000, 105, 381345),
  (100000, 4560, 5000, 93, 732574),
  (100000, 1670, 10000, 111, 8271534),
  (100000, 16530, 25000, 141, 3532368),
  (100000, 32510, 50000, 133, 2289676),
]


def gentest(n, k, p, mi, hint):
    from testy import MY_random

    T = [MY_random() % mi for _ in range(n)]
    return [T, k, p], hint
