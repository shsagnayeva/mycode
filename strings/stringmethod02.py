#!/usr/bin/env python3

def main():
  
   # create a string
   newstring = "a b c d e f"
   newlist = newstring.split(" ") # this returns a list
   print(newlist)

   # create a list of strings
   mylist = ["19252", "1100", "020", "1222"]
  
  # create a string with join() method
   singlestr = ".".join(mylist)
  
  # display singlestr
   print(singlestr)

# call our main function
main()
