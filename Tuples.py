numbers = (1, 2, 3)     # this is tuple, tuple is like a list, but we can't modify a tuple
print(numbers.count(1)) # for counting the number "1" in tuple


# UNPACKING

coordinates = (1, 2, 3)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates    # it works the same as the above three lines