try:
    int('a')
except ValueError as e:
    print("Can't do that!", e)
print("End of the program")
