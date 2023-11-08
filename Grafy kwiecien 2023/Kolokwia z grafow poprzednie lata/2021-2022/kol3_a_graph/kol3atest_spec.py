# kol3atest_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# test  n  a  b  E  S  hint
  (0, [ 7, [(0,1,5),(1,2,21),(1,3,1),(2,4,7),(3,4,13),(3,5,16),(4,6,4),(5,6,1)],[0,2,3],1,5],13),
  (1, [ 7, [(0,1,5),(1,2,21),(1,3,1),(2,4,7),(3,4,13),(3,5,16),(4,6,4),(5,6,1)],[0,2,3],1,2],1),
  (2, [ 7, [(0,1,5),(1,2,21),(1,3,1),(2,4,7),(3,4,13),(3,5,16),(4,6,4),(5,6,1)],[0,2,3],2,3],0),
  (3, [ 7, [(0,1,5),(1,2,21),(1,3,1),(2,4,7),(3,4,13),(3,5,16),(4,6,4),(5,6,1)],[0,2,3],4,5],5),
  (4, [ 7, [(0,1,5),(1,2,21),(3,4,13),(3,5,16),(4,6,4),(5,6,1)],[0,2,3],1,6],22),
  (5, [ 7, [(0,1,5),(1,2,21),(3,4,13),(3,5,16),(4,6,4),(5,6,1)],[0,2],1,6],None),
  (1500, [], 115),
  (2000, [], 131),
  (3000, [], 18),
  (5000, [], 89),
]


from testy import MY_random

def my_randint(a,b):
  return a+MY_random()%(b-a+1)

def gentest(test, arg, hint ):
  if test<6:
    return arg,hint
  
  n = test
  e = 3*n
  t = set()
  E = []
  for _ in range(e):
    u = my_randint(0,n-1)    
    v = my_randint(0,n-1)    
    if u==v: continue
    if u>v: u,v = v,u
    if (u,v) in t: continue
    t.add((u,v))
    E.append((u,v,my_randint(10,99)))
  
  S = []
  for _ in range(n//10):
    u = my_randint(0,n-1)   
    if u in S: continue
    S.append(u)

  a = my_randint(0,n-1)   
  while True:
    b = my_randint(0,n-1)   
    if b!=a: break

  return [n,E,S,a,b],hint
   

  
