import os
import re
import sys
import Valid_Logins

PATTERN = re.compile(r"^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$")

def match(PATTERN: re.Pattern, input: str) -> bool:
  if re.fullmatch(string=input, pattern=PATTERN):
    return True
  else:
    return False

      
from threading import Thread
import functools

def timeout(seconds_before_timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, seconds_before_timeout))]
            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(seconds_before_timeout)
            except Exception as e:
                print('error starting thread')
                raise e
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco

@timeout(60)
def get_password(email: str):
  while True:
    i = input("Please make a password: ")
    os.system("cls")
    print("Email: ", email)


def main():
  
  os.system("cls")
  
  while True:
    u = input("Please enter your email: ")
    os.system("cls")
    
    if match(PATTERN, u):
      break

    print("Invalid email.")
    
  print("Email: ", u)
  
  try:
    get_password(u)
  except:
    os.system("cls")
    sys.exit("Timeout!")
      
  print("reached")
      
main()