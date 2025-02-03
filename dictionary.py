#Dictionaries are mutable and contains key value pairs
#Uses hash function like sets so its just as fast
#keys are immutable. So keys cant be lists etc

#Empty dictionary
{}
print(type({}))

nums = {'one': 1, 'two': 2, 'three': 3}
print(nums['one'])

#Updating values 
nums['one'] = 100
print(nums)

colors = {"r": "Red", "g": ["Green", "Lemon Green"]}
print(type(colors["r"]))
print(nums)
#Useful if values are list..
print(type(colors["g"])) # This is a list. So list methods can be used.

colors['g'].append("Dark Green")
print(colors['g'])

#Accessing all keys and values
print(colors.keys())
print(colors.values())
print(colors.items())

#Adding and removing
nums = {'one': 1, 'two': 2, 'three': 3}
nums["four"] = 4
print(nums)

nums.pop("one") # pops the key and returns the value.
print(nums)






















