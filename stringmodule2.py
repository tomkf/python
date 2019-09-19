# From Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
 if len(s) < 3:
  return s

 verb = s[-3] + s[-2] + s[-1]
 if len(s) >= 3 and verb != "ing":
  print(s + "ing")
 elif len(s) >= 3 and verb == "ing":
  print(s + "ly") 
 
verbing("jump")




# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
 val1 = s.find("not")
 val2 = s.find("bad")
 subval = len(s) - (val2 + 3)
 substring = s[val1:-subval]
 print substring 
 if val1 < val2:
  print s.replace(substring, "good")

not_bad("This dinner is not that bad!")


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def divide_string(s):
 if (len(s) % 2) == 0:
  

def front_back(a, b):
  if ( % 2) == 0:
  return



# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))