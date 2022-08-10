#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

print(proto)

print("Index 1 element")
print(proto[1])

print("Extend method: extend list with string")
proto.extend("dns")
print(proto)

print("Append method: append string to list")
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)

print("Extend method: extend list with list")
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)

print("Append method: append list to list")
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

print("Insert method: insert string to list")
proto.insert(0, "a") # insert an item at a given index (position)
print(proto)

print("Remove method")
proto.remove("a") # remove the first irem from the list
print(proto)

print("Count method")
count = proto.count("https") # return the number of times given value appear in the list
print(count)



