import subprocess
import sys
from os import system

# p = subprocess.Popen(["dir"], shell=True)
# p = subprocess.check_output("Subprocess.py", shell=True)
p = subprocess.check_output(["echo", "Hello world!"], shell=True)
print(p)
# system("cls")

# process = subprocess.Popen(["ping", "10.20.30.173"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
for n in range(ord('a'), ord('z') + 1):
  process = subprocess.Popen([sys.executable, "Login.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  try:
    outs, errs = process.communicate(input=b"q",timeout=5)
  except subprocess.TimeoutExpired:
    process.kill()
    print("process failed")
    break
  str_outs  = outs.decode('ascii').strip("\r\n")
  print("outs: ", str_outs)
  if "incorrect" not in str_outs:
    print("The password is %c!", chr(n))
    break