def sum_of_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum


lst = {1, 2, -3, 4, 10}
print('The sum of list elements is :', sum_of_list(lst))