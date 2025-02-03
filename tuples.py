# tuples are immutable unlike lists..items cannot be changed. No append, pop, remove, insert etc.
a = ()
print(type(a))
#print(dir(tuple))

b = (1,2,3,4,5,6)
# b = 1,2,3,4,5,6 also a tuple
print(f"Lenght of b is {len(b)}")
print(f'Index of 3 is {b.index(3)}')

#Unpacking tuples

student = ("X", 100, "ComSci")
name, age, subject = student
print(name, age, subject)

def http_status_code():
    return 200, 'OK' #Tuple
code, name = http_status_code()
print (code, name)