try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:           # Exception handling for division by zero
    print("Age cannot be zero.")
except ValueError:                  # If user inputs other than numerical value
    print("Invalid value")    
