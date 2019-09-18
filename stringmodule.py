# Examples from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

def donuts(count):
  if count >= 10:
   count = "many"
  else:
   count = str(count)

  print("number of donuts: " + count)

donuts(10)

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
 if len(s) < 2:
  print("error")
 else: 
  first = s[0] + s[1]
  last = s[-2] + s[-1]
  print(first + last)

both_ends("aannbb")

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
def fix_start(s):
 target = s[0]
 isolatestring = s[1:]
 newstring = isolatestring.replace(target, "*")
 print(target + newstring)

fix_start("babble")

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'

def mix_up(a, b):
  if len(a) <= 2 or len(b) <= 2:
   print("error")
  else: 
    first = a[0] + a[1]
    last = b[0] + b[1]
    isolatefirst = a[2:]
    isolatelast = b[2:]
    print(first + isolatelast + " " + last + isolatefirst)

mix_up("pod", "mix")
