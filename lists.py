#checking functions available in lists
#print(dir(lists))

#help() Type list to show the methods available for lists in detail

#Lists in python..
lists = [2,3,1,5,4,0]

#sorting lists
lists.sort()
print(lists)

lists.reverse()
print(lists)

#append 
lists.append(100)
print(lists)

#insert 200 at index 0
lists.insert(0, 200)
print(lists)



#Extend 
odd = [1,3,5,7]
even = [2,4,6,8]
odd.extend(even)
print(odd)

#in keyword
names = ['a','b','c','d']
if ('a' in names):
    print(names.index('a'))
#update the value of the list
names[names.index('d')] = 'z'
print(names)

# Remove and Pop. Pop returns the value that is popped.
names.remove('b') # if duplicate is present, the first one is removed.
print(names)
popped = names.pop() # Can also mention the index that needs to be popped
print(names)
print(f"The item popped is {popped}")

#length of list
print(len(names))

#Slicing 
lists = [1,2,3,4,5,6,7]
print(lists[:3])
print(lists[-3:-1])