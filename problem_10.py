def reverse_string(str):
    str2 = ''
    for i in range(len(str)-1,-1,-1): # for running reverse loop
        str2 += str[i]
    return str2


string = input("Please enter any string : ")
print('The reverse of the string is :', reverse_string(string))
