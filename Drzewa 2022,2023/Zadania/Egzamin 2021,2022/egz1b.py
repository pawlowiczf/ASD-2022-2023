from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):
    # tu prosze wpisac wlasna implementacje
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )