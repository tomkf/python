# first consonant group (letters before the first vowel), and replace it with an "L".
#  Then, you put that first consonant group at the end of the word, followed by one of the louchebem suffixes
#   So "PATRON" becomes "LATRONPEM"

#words beginning with consonants ("chat", "trou"), you'll have to take the first consonant group 
#(all the letters before the first vowel) and put it at the end, add an l to the start of the word and add a suffix at the end 
#("chat" should give "latchem", or "latchoc")

# words beginning with a vowel are not changed but you should still add an l to the start of the word and a suffix at the end (
    #"atout" should give "latoutoc" or "latoutic")

#should be able to translate any complicated sentence, regardless of punctuation


suffix = ["em", "e", "ji", "oc", "ic", "uche", "es"]
# vowels = ["a", "e", "i", "o", "u", "y"]
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'z']

def louchbem_translator(str):
 if len(str) < 2:
  print("Word too small to translate")

 str_list = [x for x in str]


 const_group = []

 for char in str_list:
  if char in consonants:
   const_group.append(char)
  else: 
   break

 print(const_group)

louchbem_translator("patron")