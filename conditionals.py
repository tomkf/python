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
import sys


def contain_numers(arg):
 val = arg[1:]
 val2 = tuple(val)
 print val
 print val2

contain_numers(sys.argv)








