#sets are mutables and no duplicates are allowed..
#Kinda similar to dictionaries since sets use {}
#sets don't have an order. So can't access them by index: Type error: my_set[0]
#operations: union, difference, intersection

#Empty set:
type(set()) 

a = {1,2,3,4,4} # duplicate items will be ignored
print(a)
print(len(a))

#checking unique items in a list or tuple
lists = [1,2,3,4,1,2]
print(set(lists))

#Adding, removing from sets
my_set = {'a','b','c','d'}
my_set.add("e")
my_set.remove("d") # set.discard("d")
print(my_set)

#Union, Intersection and Difference operations
colors_one = {"Blue", "Green", "Yellow"}
colors_two = {"Blue", "Black", "Violet"}

print(f"Intersection {colors_one.intersection(colors_two)}")
print(f"Union {colors_one.union(colors_two)}")
print(f"Difference {colors_one.difference(colors_two)}")

#Sets to List
def toList(set_list):
    lists = []
    while len(set_list) != 0:
        x = set_list.pop()
        lists.append(x)
    return lists

color_set = colors_one.union(colors_two)
lists = toList(color_set)
print(lists)

#Simpler method
lists = list(colors_one) # list constructor
print(lists)

