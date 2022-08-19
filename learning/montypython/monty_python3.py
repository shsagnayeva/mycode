#!/usr/bin/python3

round = 0
answer = " "

# while loop
while round < 3  and (answer != "Brian" and answer != "Shrubbery"):
    
    # increase the round counter by 1
    round += 1
    answer = input('FInish the movie title, "Monty Python\'s The List of ______": ')

    answer =answer.capitalize()

    if answer == "Brian":
        print("Correct")
    
    elif answer == "Shrubbery":
        print("You gave the super secret answer")

    elif round == 3:
        print("Sorry, the answer was Brian")

    else:
        print("Sorry. Try again!")

        

