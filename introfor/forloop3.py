#!/usr/bin/python3

def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    
    print("\nOption1")
    for i in farms:
        print(i)

    print("\nOption2")
    for farm in farms:
        print(farm.get("name", "Unknown Farm"), end=":\n")  
                                                 
        for agri in farm.get("agriculture"):     
            print("  -", agri)    

main()

