import itertools

# method that when passed an integer above 0 returns a string containing the proper Roman numeral.
#  In other words, old_roman_numeral(4) should return "IIII".
# For reference, these are the values of the letters used:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

numerals = ["M", "D", "C", "L", "X", "V", "I"]
values = [1000, 500, 100, 50, 10, 5, 1]

def roman_numeral(num):
    roman_string = ""
    
    if num <= 0:
     print("enter valid number")

    capture_values = []

    for item in values:
     if num / item >= 1:
      capture_values.append(round(num / item))
     else: 
      capture_values.append(0)
    
    count = 0


       #iterable value     
    for counter, item in enumerate(capture_values):
     if item > 0:
      while count <= item: 
       roman_string += numerals[counter]
       count += 1

    print(roman_string)

roman_numeral(5)
