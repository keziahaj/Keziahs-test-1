'''
write a function that checks if two inputs are palindromes of one another. 
Tooltip: a palindrom is simply a word that is written backwards 
e.g 'alte' 'etla' returns YES
 '1234' '4321'
'''

# 2 arguments expected
# 1 output expected
# 2 arguments should be strings
# output should be a string
# nested for loops are not welcomed! 
# brute force method 


def palindrome(first:str, last:str)->str:

  try:
    if len(first) != len(last):
      return 'NO'
  except:
    return 'INCORRECT DATA TYPE IN ARGUMENT'

  index = -1

  for i in range(len(first)):
    if first[i] == last[index]:
      index -= 1
      continue
    else:
      return 'NO'
  return 'YES'