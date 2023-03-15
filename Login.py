from os import system

while True:
  correct_password = "q"
  u = input("Please enter your email: ")
  if "@" not in u:
    print("Invalid email. Try again.")
  else:
    i = input("Please enter your password: ")
    if correct_password == i:
      print("Login correct!")
      break
    else:
      print("Login incorrect.")