import subprocess

# p = subprocess.Popen(["dir"], shell=True)
# p = subprocess.check_output("Subprocess.py", shell=True)
p = subprocess.check_output(["echo", "Hello world!"], shell=True)
print(p)


process = subprocess.Popen(["ping", "192.168.7.229"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
try:
  outs, errs = process.communicate(timeout=5)
  print("outs: ", outs.decode('ascii').strip("\r\n"))
  print("errs: ", errs)
except subprocess.TimeoutExpired:
  process.kill()
  print("process failed")