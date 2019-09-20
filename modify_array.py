# ["Abricot du Laudot", "Black Caviar", "Brigadier Gerard"] 
# should become ["3-Brigadier Gerard!", "2-Black Caviar!", "1-Abricot du Laudot!"] after formatting.

def format_array(arr):
  final = []
  counter = len(arr)
  index = 0

  for item in arr:
    final.append(str(counter) + "-" + item + "!")
    index += 1
    counter -= 1

  print final


format_array(["Abricot du Laudot", "Black Caviar", "Brigadier Gerard"])


