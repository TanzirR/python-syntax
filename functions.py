def add_numbers(a,b = 5):
	return a+b
ans = add_numbers(3)
print(type(ans))
print(f"The sum is {ans}")


#Default operation argument is add. So no need to mention explicitly.
def calc (a, b, operation = "add"):
	if operation == "sub":
		return a-b

print (calc(2,13))
print (calc(2,13, "sub"))


