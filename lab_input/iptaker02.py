#!/usr/bin/env python3

# print string
def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address: ")
    
    ## the line below creates a single string that is passed to print()
    #print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is: ", user_input)

    vendor = input("Please enter the vendor name: ")
    print(f"Vendor name is {vendor}")

main()

