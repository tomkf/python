import sys
import math 

#challenges taken from: https://github.com/zhiwehu/Python-programming-exercises

#find all numbers which are divisible by 7 but not a multiple of 5 between 2000 and 3200 
#should be printed comma seperated on a single line 


def divisible():
 collection = list(range(2000, 3200))
 filteredcollection = []
 for item in collection:
  if item % 7 == True and item % 5 == False:
    filteredcollection.append(item)
 print(str(filteredcollection)[1:-1])

divisible()


#compute factorial of a given number 
# results printed in comma seperated sequence of a single line 
# ie; 8 as an argument render 40320


def factorial(num):
 if num == 0:
  return 1
 counter = 1
 collection = []
 val = 1
 while counter <= 8: 
  collection.append(counter)
  counter += 1
 for item in collection: 
  val = item * val
 print val

factorial(8) 


# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def integral(num):
 collection = {}
 valcollection = list(range(1, num + 1))
 indexcounter = 1 
 for value in valcollection:
  collection[indexcounter] = value * indexcounter
  indexcounter += 1
 print collection

integral(8)


# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


def contain_numers():
  arg = raw_input("enter  collection of numbers")
  fin1 = arg.replace(" ", "")
  fin2 = fin1.replace(",", "")
  val2 = tuple(fin2)
  print arg
  print val2

contain_numers()


# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class MyClass:
  def __init__(self):
    self._my_string = ""
   
  def getString(self): 
   userstring = raw_input("enter input")
   self._my_string = userstring
 
  def printString(self):
   print(self._my_string.upper())

test = MyClass()
test.getString()
test.printString()


# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24


def calculate_square(sys_array):
 final_value = " "
 
 for item in sys_array:
  value = math.sqrt(2 * 50 * int(item) / 30)
  final_value += str(round(value))
  final_value += " "

 print(final_value)

 
val = input("enter a collection of numbers: ")
convert = val.split(',')
calculate_square(list(convert))


#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 


def dimensional_array(x,y):
 final_array = []
 multiple = 0
 counter = 0

 while counter < x:
  sub_array = []
  sub_count = 0 
  while sub_count < y:
   sub_array.append(multiple * sub_count)
   sub_count += 1
  
  multiple += 1
  counter += 1
  final_array.append(sub_array)

 print(final_array)

dimensional_array(3, 5)


#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world


def sort_wordgroup(my_str):
 convert = my_str.split(",")
 convert.sort()
 final = ",".join(convert)
 print(final)

sort_wordgroup("without,hello,bag,world")
