# Dictionary is collection of key-value pairs
# its unordered
# its mutable
# indexed as per key
# duplicate keys not allowed
# can be coverted to list

dt = {
    "Fast": "Something in hurry",
    "Jay": "Is a coder", 
    "Marks": [4,7,54], # valid---
    "otherdict": { #-- also valid nested dictionary
        'harry': "Barry",
        'joy': "Granny"
        }
}

print(dt["Fast"])
print(dt["Jay"])
print(dt["Marks"])
print(dt["otherdict"])
print(dt["otherdict"]['joy'])