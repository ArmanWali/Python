def vowel_calculator(str):
    count = 0
    for i in range(len(str)):
        if str[i] == 'A' or str[i] == 'E' or str[i] == 'I' or str[i] == 'O' or str[i] == 'U':
            count += 1
    return count


string = input('Please enter a string : ')

print('The number of vowels in this string is :',vowel_calculator(string.upper()))