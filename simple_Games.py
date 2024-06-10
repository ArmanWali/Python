# Excercise "Car Game"

    
choice = ' '
started = False

while choice != 'QUIT':
    choice = input('>').upper()
    if choice == 'START':
        if started:
            print('Car is already starded!')
        else:
            started = True
            print('Car started...')       
    elif choice == 'STOP':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print('Car stopped.')
    elif choice == "HELP":
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif choice == 'QUIT':
        break
    else:
        print("I don't understand that...")