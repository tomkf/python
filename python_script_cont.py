import sys

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


# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010


def binary_check(user_input):
 
 for item in user_input:
   if item % 5 == 0:
     print(item)

binary_check(input("enter a collection of 4 digit binary numbers"))


# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


def char_counter(str):

  user_letters = 0
  user_array = str.split()

  for item in user_array:
    user_letters += len(item)
  
  print("WORDS: %s" % len(user_array))  
  print("LETTERS: %s" % user_letters)

char_counter(input("enter a your words (include quotation marks): "))


# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.


def case_counter(str):
  convert = list(str)
  low_case = 0
  up_case = 0
  
  for char in convert:
    if char.islower() == True:
      low_case += 1
    elif char.isupper() == True:
      up_case += 1

  print("Upper case: %s" % up_case)
  print("Lower case: %s" % low_case)

case_counter("Hello world!")


# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input.
#  The transaction log format is shown as following:
# D (x)
# W (x)


