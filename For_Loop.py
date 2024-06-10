for item in ['Arman','Sinan','Momin','Taimur']:
    print(item)        # prints the above names in seperate lines

for num in range(10):
    print(num)         # prints the numbers from 0 to 9

sum = 0
for num in [10, 20, 30]:    # for loop to add the numbers
    sum += num
print(f"Total sum = {sum}")  # total sum will be equal to 60

# nested loops

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')


# Challenge Exercise

numbers = [2,2,2,2,6]

for i in numbers:
    output = ''
    for j in range(i):
        output += 'X'
    print(output)

print(range(i))