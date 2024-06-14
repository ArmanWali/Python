def Max_num_finder(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

numbers_list = [1, 2, 3, 4, 500, -10, 20, 0, 50]
print(Max_num_finder(numbers_list))
