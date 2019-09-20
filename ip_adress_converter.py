binary = [128, 64, 32, 16, 8, 4, 2, 1]  

def binary_calculator(bin_str):
 collection = list(bin_str)
 working_total = len(bin_str)
 counter = 0
 working_val = collection[counter]
 complete_vals = []

 while working_total >= 0:
  sum = working_val * (2 ** working_total)
  complete_vals.append(sum)
  counter += 1
  working_total -= 1
  
 print(complete_vals)
 

#that takes an ip address string and converts it to a number
def ip_to_num(ip):
 convert = ip.split(".")
 counter = 0
 binary_string = ""

 while counter < len(convert):
  working_int = int(convert[counter]) 
  for bin_val in binary:
   if working_int - bin_val < 0:
    binary_string += "0"
   elif working_int - bin_val >= 0: 
    binary_string += "1"
    working_int -= bin_val
  counter += 1

 print binary_string
 binary_calculator(binary_string)
 
 

ip_to_num("37.160.113.170")
# => 631271850



#takes a number and converts it to an IP address string.
# def num_to_ip(val):
#  convert_array = list(str(val))
#  counter = 0 
#  binary_collection = ""

#  for bin_value in binary:
#   subval = int(convert_array[counter]) - bin_value 
#   if subval >= 0:
#    binary_collection + str(subval)
#   else: 
#    binary_collection += ""
#  counter += 1

#  print(binary_collection)


# num_to_ip(631271850)
# => "37.160.113.170"
    