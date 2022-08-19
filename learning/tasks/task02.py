#!/usr/bin/env python3

def list_func():
    
    # create a list
    list_result = []

    # create lists
    list1 = ["Pasta", "Risotto", "Pizza", "Ravoili", "Fettuccine"]
    list2 = ["Parmesan", "Provolone", "Mascarpone", "Mozzarella"]
    list3 = ["Gelato", "Tiramisu"]

    # append lists to list
    list_result.append(list1)
    list_result.append(list2)
    list_result.append(list3)

    print (list_result)
    print(list_result[0][1])

list_func()


def dict_func():
    
    # create a dictionary
    dict1 = {"quality1": "example1", "qulity2": "example2", "quality3": "example3"}
    
    # print keys
    print(dict1.keys())

    # print values
    print(dict1.values())

dict_func()


