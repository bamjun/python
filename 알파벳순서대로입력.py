def listAlphabet1():
  return list(map(chr, range(97, 123)))
print (listAlphabet1())

def listAlphabet2():
  return [chr(i) for i in range(97, 123)]
print(listAlphabet2())

def listAlphabet3():
  return [chr(i) for i in range(ord('a'), ord('z')+1)] 
print(listAlphabet3())

import string
def listAlphabet4():
  return list(string.ascii_lowercase)
print(listAlphabet4())
