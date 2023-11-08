# kol3atest_spec.py
end = None

ALLOWED_TIME = 1000

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow
  end
end

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# test  T  hint
  (0, [0,1,2,3,4,10,22], 2),  # dane z tematu zadania
  (1, [0,1,2,3,4,5,6], 0),    # drzewo pelne o 3 poziomach  
  (2, [0,1,2,3,4,5,10], 1),  
  (3, [0,1,2,3,4,5,6,7,8,9,10,11], 1),  
  (4, [0,1,2,3,6,7,15,16,31,34], 1),  
  (5, [0,1,2,3,4,6,7,8,15,16,31,32,34,63], 4),  
  (10,[],106),
  (13,[],847),
  (16,[],7007),
  (20,[],111776),
]


from testy import MY_random

def my_randint(a,b):
  return a+MY_random()%(b-a+1)


def gentest(test, arg, hint ):
  # print('===',test,arg,hint)
  if test<6:
    T = [None for _ in range(len(arg))]
    for i in range(len(arg)): T[i] = Node()

    for i,n in enumerate(arg):
      left = 2*n+1
      if left in arg: T[i].left = T[arg.index(left)]
      right = 2*n+2
      if right in arg: T[i].right = T[arg.index(right)]
    end
  else:
    n = 2**test
    T = [None for _ in range(n)]
    for i in range(n):
      if my_randint(0,9)<2: T[i] = Node()
    for i in range(n-1,0,-1):
      if T[i]!=None:
        if T[(i-1)//2]==None: T[(i-1)//2] = Node()

        if i%2==1: T[(i-1)//2].left = T[i]
        else: T[(i-1)//2].right = T[i]
    '''
    print('dane: ',end='')
    for i in range(n):
      if T[i]!=None: print(i,end=' ')
    print()
    '''
  end    

  return T[0],hint
  
   

  
