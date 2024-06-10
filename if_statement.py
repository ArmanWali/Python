is_hot = True
is_cold = False

if is_hot:   # if statement will be printed because the condition is true
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")    # this will also be printed because it is not the part of any condtion

# Exercise question

has_goodCredits = False

if has_goodCredits:
    print("The price is 10% off and is : $",1000000-(.1*1000000))
else:
    print("The price is 20% off and is : $",1000000-(.2*1000000))  # else part will be printed because condtion is false

# logical operators

has_high_income = False
has_good_credits = True

if has_high_income and has_good_credits:
    print("Eligible for loan!")
else:
    print('Not eligible for loan!')   # this part of code will be executed because one of the condition is wrong

if has_high_income or has_good_credits:
    print('Eligible for loan!')       # this will print because one of the condition is true
else:
    print('Not eligible for loan!')

has_criminal_record = False

if has_good_credits and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan')