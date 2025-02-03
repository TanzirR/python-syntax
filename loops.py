colors = ['red','green','blue']

#for loop
for color in colors:
    print(color)

#Range
for i in range(len(colors)):
    print(colors[i])

lists = [1,2,3,4,5,6]
for i in range(1,5): #5 is exlcuded 
    print(lists[i])

print("Include a step of 2 in range")

for i in range (1,5,2):
    print(lists[i])

# Looping over Dictionary 
hex_colors = {"Red": "#FF", "Green": "#008"}
for color, hex in hex_colors.items(): #.items returns a tuple of key values, so it can be unpacked
    print(f"The color is {color} and the hex value is {hex}")

#Enumerate => returns the index and the value
for i, color in enumerate(colors):
    print(f"Index: {i}, color: {color}")

#While loop
counter = 0
max = 5
while counter < max:
    print(counter)
    counter += 1

# break, continue, return in loops




