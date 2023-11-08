# zad3test_spec.py

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]


TEST_SPEC = [
  (10, 5, 3, 0),
  (100, 20, 5, 5),
  (1000, 100, 5, 5),
  (1001, 100, 50, 50),
  (10002, 100, 5, 11),
  (10002, 100, 50, 51),
  (20001, 100, 5, 80),
  (30002, 5, 50, 366),
  (50000, 50, 5, 31),
  (50002, 100, 50, 84),
]


def gentest(n, max_w, max_s, hint):
    from testy import MY_random

    T = []
    i = 0
    while i < n:
        k = MY_random() % max_w + 1
        s = MY_random() % (max_s + 1)

        w = ''.join([chr(97 + (MY_random() % 26)) for _ in range(k)])
        T.append(w)
        i += 1

        for _ in range(s):
            if i == n: break
            if MY_random() % 2 == 0:
                T.append(w)
            else:
                T.append(w[::-1])
            i += 1

    if n % 10 == 1:
        w = ''.join([chr(97 + (MY_random() % 26)) for _ in range(100000)])
        T[-1] = w
    idx = [MY_random() % n for _ in range(n)]
    for i, pos in enumerate(idx):
        tmp = T[i]
        T[i] = T[pos]
        T[pos] = tmp
    if n % 10 == 2:
        T.sort(reverse = True)

    return [T], hint

