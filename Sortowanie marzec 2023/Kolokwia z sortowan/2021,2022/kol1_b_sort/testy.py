# testy.py
# from signal import signal, alarm, SIGALRM

import sys

TIMER = False
RERAISE = True
PRINT_STATUS = False
USE_STORED_TESTS = False
SAVE_TESTS = False
FORCE_ALL_TESTS = False


if TIMER:
  from signal import signal, alarm, SIGALRM

from copy import deepcopy
import time


if USE_STORED_TESTS:
  from STORED_TESTS import STORED_TESTS



def print_err(*a):
     print(*a, file = sys.stderr)
 

MY_seed    = 42
MY_a       = 134775813
MY_c       = 1
MY_modulus = 2**32
def MY_random():
   global MY_seed, MY_a, MY_c, MY_modulus
   MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
   return MY_seed





# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]



def list2str( L ):
  s = ""
  for x in L:
    s += str(x) +", "
  s = s.strip()
  if len(s) > 0: 
    s = s[:-1]
  return s

def limit( L, lim=120 ):
  x = str( L )
  if len(x) < lim:
    return x
  else:
    return x[:lim]+"[za dlugie]..."

    
    
class TimeOut(Exception):
  def __init__(self):
    pass
    
    
def timeout_handler( signum, frame ):
   raise TimeOut()


def internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ACC_TIME ):
  passed, timeout, answer, exception = 0, 0, 0, 0


  if USE_STORED_TESTS:
    TESTS = STORED_TESTS
  else:
    if all_tests or FORCE_ALL_TESTS:
      TESTS = generate_tests()
    else:
      TESTS = generate_tests(3)


  if SAVE_TESTS:
    file = open("STORED_TESTS.py","w")
    file.write(f"STORED_TESTS = {TESTS}")

  # A - Accepted
  # T - Timeout
  # W - Wrong Answer
  # E - Exception when solving
  # O - Terminated by operator
  status_line = ''

  total  = len(TESTS)
  total_time = 0
  for i,d in enumerate(TESTS):
    print("-----------------")
    print("Test", i )
    arg  = copyarg(d["arg"])
    arg2 = copyarg(d["arg"])
    hint = deepcopy(d["hint"])
    printarg( *arg )
    printhint( hint )
    try:
      if TIMER:
        signal( SIGALRM, timeout_handler )
        alarm( ACC_TIME + 1)
      time_s = time.time()
      end    = time.time() 
      sol    = f( *arg )
      time_e = time.time()
      
      if TIMER:
        alarm(0)
      printsol( sol )
      res = check( *arg2, hint, sol )
      if ACC_TIME > 0 and float(time_e-time_s) > ACC_TIME:
        timeout += 1
        status_line += ' T'
        print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
      elif res:
        passed += 1
        status_line += ' A'
        print("Test zaliczony!")
      else:
        answer += 1
        status_line += ' W'
        print("TEST NIEZALICZONY!!!")
      print("Orientacyjny czas: %.2f sek." % float(time_e-time_s))
        
      total_time += float(time_e-time_s)
    except TimeOut:
      timeout += 1
      status_line += ' T'
      print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
    except KeyboardInterrupt:
      exception += 1
      status_line += ' O'
      print("Obliczenia przerwane przez operatora")
    except Exception as e:
      exception += 1
      status_line += ' E'
      print("WYJATEK:", e)
      if RERAISE: raise e
    
    
  print("-----------------")
  print("Liczba zaliczonych testów: %d/%d" % (passed,total) )
  print("Liczba testów z przekroczonym czasem: %d/%d" % (timeout,total) )
  print("Liczba testów z błędnym wynikiem: %d/%d" % (answer,total) )
  print("Liczba testów zakończonych wyjątkiem: %d/%d" % (exception,total) )
  print("Orientacyjny łączny czas : %.2f sek." % total_time )
  print("Status testów:%s" % status_line )

  if PRINT_STATUS: print_err(sys.argv[0].replace("_"," ").replace(".py",""), passed, total, "%.2f" % total_time, status_line)
