my_data = "This,is,a,comma,separated,string"
print(type(my_data))

#String split creats a list
print(my_data.split(",")) # retuns a list
student_info = "A,100,CompSci"
name, age, sub = student_info.split(",")
print(f"Name: {name}, age: {age}, subject: {sub}") #List unpacking, same as tuple unpacking

#String join takes in a list
student_info_list = student_info.split(",")
student_info_join = ','.join(student_info_list)
print(student_info_join)

# Converting between strings and int
print("Today is the " + str(20) + "th")
str_num = "50"
print(50 + int(str_num))
#float()
float(str_num)

#Converting to a list
greeting = "Hello"
greeting_list = list(greeting)
print(greeting_list)
print("".join(greeting_list))

