from zad2testy import runtests

def fast_list_prepend(L,a):
    # tu prosze wpisac wlasna implementacje
    return FastListNode(a)


class FastListNode:
  def __init__(self, a):
    self.a = a     # przechowywana liczba calkowita
    self.next = [] # lista odnosnikow do innych elementow; poczatkowo pusta

  def __str__(self): # zwraca zawartosc wezla w postaci napisu
    res = 'a: ' + str(self.a) + '\t' + 'next keys: '
    res += str([n.a for n in self.next])
    return res




runtests( fast_list_prepend ) 
