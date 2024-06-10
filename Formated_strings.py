first = 'Arman'
last = 'Wali'
message = first + ' [' + last + '] is a coder\n'    # not a good method to add the strings
print(message)

msg = f'{first} {last} is a coder'                # formated string method
print(msg)