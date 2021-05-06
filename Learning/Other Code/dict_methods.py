dt = {
    "fast": "Something in hurry",
    "jay": "Is a coder", 
    "marks": [4,7,54], # valid---
    "otherdict": { #-- also valid nested dictionary
        'harry': "Barry",
        'joy': "Granny"
        },
    1 : 2

}

print(list(dt)) #-- typecasting to list

print(dt.keys()) # -- to print all keys defined
print(dt.values()) #- to print all values associated with keys

print(dt.items()) # -- prints all key,value for all contents of dictionary returns a tuple

print(dt)
up = {
    "jhonny": "friend",
    "koli": "maharashtra"
} # other dict

dt.update(up) # appends key-value pairs at last location, 
# will update if any same key is updated with any value
print("After Update: ",dt)

#----------------------------------------------# IMPPPP

print(dt.get("jay")) # returns value for the given key, 
                     # doesnt throw error if key not present its none
# print(dt["jay2"]) # throws error if key not present