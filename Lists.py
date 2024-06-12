names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[1:-1])  # printing the middle 3 names

# Exercise Question (finding the largest number in a list)

numbers = [-9, 2, -3, 10, -5]
max = numbers[0]     # assuming that max number is the first number in the list
for n in numbers:    # for loop for iterating through the list numbers
    if n > max:
        max = n      # if a number is greater than max, then max will be updated and take the value of the number

print(max)           # printing the largest number of the list

# 2D lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][1])    # this will print the number "5"

for row in matrix:     # for loop for printing all the values in the matrix
    for columns in row:
        print(columns)

# removing duplicates from a list

list = [1, 1, 2, 2, 3, 4, 4, 10, 5]
unique = []

for nums in list:
    if nums  not in unique:
        unique.append(nums)

print(unique)

