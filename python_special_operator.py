x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # True if the operands are not identical (do not refer to the same object)

print(x2 is y2)  # True if the operands are identical (refer to the same object)

print(x3 is y3)  # prints False

# Here, we see that x1 and y1 are integers of the same values, so they are equal as well as identical.
# The same is the case with x2 and y2 (strings).
# But x3 and y3 are lists. They are equal but not identical.
# It is because the interpreter locates them separately in memory, although they are equal.