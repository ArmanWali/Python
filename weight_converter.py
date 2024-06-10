weight = float(input("Please enter your weight : "))
unit = input("L=pounds  or  K=Kg : ")

if unit.upper() == 'L':
    print('You are ',weight/2.20462,' kg ')
else:
    print('You are ',weight*2.20462,' pounds ')