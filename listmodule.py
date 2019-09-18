# From Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.

def match_ends(words):
  count = 0 
  for word in words:
   if len(word) <= 2 and word[0] is word[-1]:
    count += 1
  print(count)

match_ends(["a", "dog", 'racecar', "running"])

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

def front_x(words):
 firstarr = []
 secondarr = []
 words.sort()
 for word in words:
   if word[0] is "x":
    firstarr.append(word)
   else: secondarr.append(word)
 print firstarr + secondarr

front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])



# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def sort_last(tuples):
 return sorted(tuples, key=last)

sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])