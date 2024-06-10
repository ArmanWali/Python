i = 1

while i <=5:
    print('*' * i)
    i += 1
print('Done\n\n')

# Exercise "Guessing Game"

secret_number = 9
guess_count = 0
guess_limit = 3
print('Please guess a number')
while guess_count < guess_limit:         # while loop for guessing the number upto 3 times
    Guess = int(input("Guess: "))
    guess_count += 1
    if Guess == secret_number:           # checking whether the guess is correct or not
        print('Right Guess, You won!')
        break
else: 
    print('Sorry you Failed')            # else part of the while loop





    
