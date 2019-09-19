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
 
