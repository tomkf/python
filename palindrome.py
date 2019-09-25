import sys

def palindrome(usr_input):
    answer_a = "It's a palindrome baby"
    answer_b = "Not a palindrome buddy"

    if (len(usr_input) % 2) == 0:
        if usr_input[::-1] == usr_input:
            print(answer_a)
        else:
            print(answer_b)

    else:         
        num_val = len(usr_input) / 2
        val = usr_input[num_val]
        working_val = usr_input.split(val)
        
        if working_val[0][::-1] == working_val[1]:
            print(answer_a)
        else: 
            print(answer_b)

palindrome(input("enter a word (include quotation marks)"))