#Author: Kyle Chen kvc5823@psu.edu  
#Collaborator:
#Collaborator:
#Collaborator: 
#Breakout Room:
#Section: 10

def is_palindrome1(s):
  i = len(s) - 1
  j = 0
  while (j < i):
    if(s[j] != s[i]):
      func1 = False
    i = i - 1
    j = j + 1
  return func1

def is_palindrome2(s):
  func2 = True

  if(len(s) - 1 <= 0):
    return func2
  if(s[0] == s[len(s) - 1]):
    changed = s[1:-1]
    return(is_palindrome2(changed))
  else:
    func2 = False
    return func2

def is_palindrome3(s):
  return(s == s[::-1])

def run():
  s = input("Enter a string: ")
  print(is_palindrome1(s))
  print(is_palindrome2(s))
  print(is_palindrome3(s))

if __name__ == "__main__":
  run()

 