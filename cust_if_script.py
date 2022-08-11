#!/usr/bin/env python3

def main():

    result = "Hurricane category is "
    
    while True:

        speed = input("Please enter wind speed (mph): ")
        
        try:

            speed = float(speed) 
            if speed >= 157:
                result = result + "five"
            elif speed >= 130 and speed <= 156:
                result = result + "four"
            elif speed >= 111 and speed <= 129:
                result = result + "three"
            elif speed >= 96 and speed <= 110:
                result = result + "two"
            elif speed >= 74 and speed <= 95:
                result = result + "one"
            elif speed >= 0 and speed < 74:
                result = "Not a hurricane"
            else:
                result = "Negative number provided. Please run program again and enter positive number"
            
            print(result)
            print("Exiting program\n") 
            break

        except ValueError:
            
            print("Please enter number")

main()
