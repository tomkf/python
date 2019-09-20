# ["Abricot du Laudot", "Black Caviar", "Brigadier Gerard"] 
# should become ["3-Brigadier Gerard!", "2-Black Caviar!", "1-Abricot du Laudot!"] after formatting.

def format_array(arr):
  modify = []
  final = []
  counter = len(arr)
  index = 0

  for item in arr:
    modify.append("-" + item + "!")

  for item in modify:
    final.append(str(counter) + modify[index])
    index += 1
    counter -= 1

  print final


format_array(["Abricot du Laudot", "Black Caviar", "Brigadier Gerard"])


