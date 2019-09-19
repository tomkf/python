import sys

def coaching():
 get_input = input("tell me what to do")
 if get_input == "I am going to work right now!":
  print("goodbye!")
 elif get_input[-1] == "?":
  print("Silly question, get dressed and go to work!")
 else:
  print("I don't care, get dressed and go to work!")

coaching()