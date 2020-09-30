#Author: Kyle Chen kvc5823@psu.edu  
#Collaborator:
#Collaborator:
#Collaborator:

def is_palindrome1(s):
  counter=0
  revste=s[::1]
  for i in range (0,len(s),1):
    if revste[1]==s[1]:
      counter+=1
    else:
      counter+=0
  if counter == len(s):
    return True
  else:
    return False
    