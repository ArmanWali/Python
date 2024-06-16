def is_prime(num):
    if num <= 1:
        print('Not a prime number')
    elif num == 2:
        print('Prime Number')
    elif num > 2:
        for i in range(2,num):
            if num % i == 0:
                print('Not a prime number')
                return
            else:
                print('Prime number')
                return


number = int(input('Enter a number : '))
if number < 0:
    print('Please Enter a positive number : ')
    
else:
    is_prime(number)
