# kolutest_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n  m  hint
    (10, 3, 3),
    (100, 10, 10),
    (500, 50, 75),
    (1000, 100, 141),
    (2000, 200, 273),
    (3000, 500, 488),
    (5000, 500, 650),
    (5000, 1000, 955),
    (10000, 1000, 1419),
]


from testy import MY_random


def gentest(n, m, hint ):
    order = [i for i in range(n)]
    for i in range(n):
        j = MY_random() % n
        order[i], order[j] = order[j], order[i]

    d = ['A', 'B']
    disk = [d[MY_random() % 2] for _ in range(n)]

    deps = [[] for _ in range(n)]
    for i in range(1, n):
        dlen = MY_random() % (m+1)
        dlen = min(i, dlen)
        deps[order[i]] += list(set([order[MY_random() % i] for _ in range(dlen)]))

    return [disk, deps], hint
