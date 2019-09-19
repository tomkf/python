# method colorful which takes a number as argument and return true if the number is colorful, false otherwise.
# A colorful number is a number where all the products of consecutive subsets of digit are different.
# For this exercise, only consider numbers with up to 3 digits (not more).

def colorful(num):
 digits = list(str(num))
 collection = []

 for digit in digits:
  collection.append(int(digit))

 product_1 = collection[0] * collection[1]
 product_2 = collection[1] * collection[2]
 product_3 = collection[0] * collection[1] * collection[2]
 if product_1 != product_2 and product_1 != product_3 and product_2 != product_3:
  print("true")
 else:
  print("false")

colorful(263)
colorful(236)