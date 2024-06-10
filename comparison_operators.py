temperature = 35

if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


# Exercise Question

name = input("Enter your name : ")

if len(name) < 3:   # if the name is less than 3 characters long
    print("Name must be at least 3 characters")
elif len(name) > 50:  # if the name is more than 50 characters long 
    print("Name can be maximum of 50 characters")
else:
    print('Name looks good!')