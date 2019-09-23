# Challenges taken from: 
# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt


# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words
# and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world


def remove_whitespace(str):

 str_array = str.split(" ")

 for item in str_array:
   if str_array.count(item) > 1:
    str_array.remove(item)
 
 str_array.sort()
 print(' '.join(str_array))


remove_whitespace("hello world and hello world again")
