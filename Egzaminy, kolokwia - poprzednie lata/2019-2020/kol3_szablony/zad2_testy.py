from zad2 import *


def insert(hash_tab, key):
    idx = h(key)
    for i in range(N):
        if hash_tab[idx].taken:
            idx = (idx + 1) % N
        else:
            break
    
    if not hash_tab[idx].taken:
        hash_tab[idx].key = key
        hash_tab[idx].taken = True


def find(hash_tab, key):
    idx = h(key)
    for i in range(N):
        if not hash_tab[idx].taken: return None
        if hash_tab[idx].key == key: return idx
        idx = (idx + 1) % N
    
    return None


test_keys = ['Jan', 'Anna', 'Piotr', 'Zofia', 'Witold', 'Irena', 'Marek', 'Monika']


for i in range(N):
    hash_tab[i].key = None
    hash_tab[i].taken = False

for k in test_keys:
    insert(hash_tab, k)

tab = [(str(hash_tab[i].key),
        str(hash_tab[i].taken),
        h(hash_tab[i].key) if hash_tab[i].taken else ' -'
       ) for i in range(N)]

print('Zawartosc tablicy:\t # key, taken, h(key)\n')
for e in tab:
    print('{:10}\t{:5}\t{:2}'.format(e[0], e[1], e[2]))
print('--------------------------')


for tnum, nuked in enumerate([10, 6, 3, 2]):
    usuniety = hash_tab[nuked].key
    log = 'Test {0:1d}: Usunieto {1:10s}\t-\t'.format(tnum+1, usuniety)
    
    hash_tab[nuked].key = None
    hash_tab[nuked].taken = False
    
    recover(hash_tab)
    
    M = []
    for k in test_keys:
        if k != usuniety and find(hash_tab, k) is None:
            M.append(k)
    
    if len(M) > 0:
        log += 'Niedostepne: ' + ' '.join(M)
    else:
        log += 'Tablica prawidlowa'
    
    print(log)
    
    for i in range(N):
        hash_tab[i].key = None
        hash_tab[i].taken = False
        
    for k in test_keys:
        insert(hash_tab, k)
