#!/usr/bin/env python3

def main():

    result = "Hurricane category is "

    speed = int(input("Please enter wind speed (mph): "))
    
    if speed >= 157:     
        result = result + "five"
    elif speed >= 130 and speed <= 156:
        result = result + "four"
    elif speed >= 111 and speed <= 129:
        result = result + "three"
    elif speed >= 96 and speed <= 110:
        result = result + "two"
    elif speed >= 74 and spped <= 95:
        result = result + "one"
    elif speed < 74:
        result = "Not a hurricane"
    else:
        result = "Please provide wind speed"
    print(result)

main()
