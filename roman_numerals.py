import math

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
      capture_values.append(math.trunc(num / item))
     else: 
      capture_values.append(0)
    
    working_value = 0 
    first_val = filter(lambda x: x > 0, capture_values)
    first_occurrence= list(first_val)[0]

    index_location = capture_values.index(first_occurrence)
    working_value = values[index_location] * first_occurrence
    complete_val = num
   # print(complete_val)
    #print(working_value)

    for counter, item in enumerate(capture_values):
     # while complete_val > 0:
      print(item)
      if complete_val >= values[counter]:
        roman_string += numerals[counter]
        complete_val -= values[counter]
        print(complete_val)
    
    print(capture_values)
    print(roman_string)

roman_numeral(8)
