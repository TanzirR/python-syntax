#Shorter way to loop and do something in a list;  lists = ["do something" for num in lists]

# Square the numbers in the list
lists = list(range(6))
print(lists)

lists_double = [num * num for num in lists]
print(lists_double)

#to upper case 
fruits = ["apple", "banana", "orange"]
fruits_to_upper = [fruit.upper() for fruit in fruits]
print(fruits_to_upper)

#return a tuple
fruits_tuple = [("length", len(fruit)) for fruit in fruits]
print(fruits_tuple)

#Conditions 

#Create a list of even numbers
lists = [1,2,3,4,5,6,7,8]
lists_even = [num for num in lists if num % 2 == 0]
print(lists_even)

# create the above even numbers to string
list_even_to_str = ",".join([str(even_num) for even_num in lists_even])
print(list_even_to_str)

# built in operations: sum, min, max, sorted
print(f"The sum of even num: {sum(lists_even)}")
print(f"The min of even num: {min(lists_even)}")
print(f"The max of even num: {max(lists_even)}")
print(f"Even num sorted: {sorted(lists_even, reverse = True)}")

#strings to int
lottery_num_string = "4,5,6,7,8"
lottery_num_int = lottery_num_string.split(",")
lottery_num_int = [int(num) for num in lottery_num_int]
print(lottery_num_int)
print(f"Max num: {max(lottery_num_int)}")

