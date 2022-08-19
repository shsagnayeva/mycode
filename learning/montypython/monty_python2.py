#!/usr/bin/env python3

# integer initiated to 0
round = 0

# while loop condition
while True: 
    
    round = round + 1

    print('Finish the movie title, "Monty Python\'s The Life of ______"')

    answer = input("Your guess--> ")

    if answer == "Brian":
        print("Correct")
        break

    elif round == 3:
        print("Sorry, the answer was Brian.")
        break

    else:
        print("Sorry! Try again!")




