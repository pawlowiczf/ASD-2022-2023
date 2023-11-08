class Node:
    def __init__(self, key = None, taken = False):
        self.key = key
        self.taken = taken
        
    def __str__(self):
        if not self.taken:
            print('pusty')
        else:
            print('klucz: ', self.key)


def h(key):
    v = int('0b10101010', 2)
    for l in key:
        v ^= ord(l) % 255
    
    return v % N


N=11
hash_tab = [Node() for i in range(N)]


def recover(hash_tab):
    1 / 0 # zamienic na prawidlowa implementacje
