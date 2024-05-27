name = 'Arman Wali'
greeting = 'Hello'

print(name.upper())             #to uppercase the string
print(name.count("Arman"))      #to count the specific words or characters
print(name.find('Arman'))       #returns the index of the word

new_name = name.replace('Arman', 'Wali')   #to replace one word with another one
print(new_name)

message = greeting + ", " + name                      #adding two or more strings
message = '{}, {}, welcome!'.format(greeting, name)   #function to avoid the above + signs
print(message)

message = f'{greeting}, {name}. Welcome!'             #using f streams for the above
print(message)

print(dir(name))                          #all function we have access to with that variable
print(help(str))                          #gives description of the methods or functions