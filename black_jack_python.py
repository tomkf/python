import random 

def run_game():
 bank_score = random.randint(16, 24)
 print "The banks scor is: "
 print bank_score
 cards = 0
 round = 0
 player_score = 0

 while player_score <= 21:
  user_submit = input("What do you want to do: (type answers as stings) a: draw card press b: settle game")
  user_val = user_submit

  if user_val is "a": 
   card = random.randint(1, 11)
   player_score += card
   print "Your score:"
   print player_score

  elif user_val is "b" and player_score > bank_score:
   print("You win")
   player_score += 24

  elif user_val is "b" and player_score < bank_score:
   print("You loose")
   player_score += 24
   
  elif user_val is "b" and player_score == bank_score:
   print("draw")
   player_score += 24
   
  if player_score == 21:
   print("you win")
   player_score += 1

  elif player_score > 21:
   print("you loose")
   player_score += 24
 
run_game()