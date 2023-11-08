# kol1btest_spec.py

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  (10, 4, 8),
  (10, 9, 800),
  (100, 6, 1000),
  (100, 80, 10000),
  (100, 80, 10000),
  (1000, 500, 1000),
  (1000, 5, 1000),
  (5000, 5000, 1000),
  (10000, 500, 10),
  (10000, 10, 10),
]

from testy import MY_random

def shuffle(word):
    chars = list(word)
    for i in range(len(word)):
        x = MY_random() % len(word)
        y = MY_random() % len(word)
        chars[x], chars[y] = chars[y], chars[x]
    return ''.join(chars)

def randomWord(length):
    chars = []
    for i in range(length):
        chars.append(chr(ord('a') + (MY_random() % (ord('z') - ord('a') + 1))))
    return ''.join(chars)

def gentest(N, maxRes, maxLen):
    R = []
    words = set()
    maxcnt = 0
    while len(R) < N:
        cnt = min(MY_random() % (maxRes - 1) + 1, N - len(R))
        maxcnt = max(cnt, maxcnt)
        length = MY_random() % (maxLen-1) + 1
        word = ''.join(sorted(randomWord(length)))
        if word in words: continue
        words.add(word)
        R.extend([shuffle(word) for _ in range(cnt)])

    for i in range(len(R)):
        x = MY_random() % len(R)
        y = MY_random() % len(R)
        R[x], R[y] = R[y], R[x]

    return [R], maxcnt
    
