def factorial(n):
    fact = 1
    if n < 0:
        return n
    else:
        for i in range(1,n+1):
            fact = fact * i
        return fact


num = int(input('Please enter a number : '))
print('The factorial of the number is :', factorial(num))