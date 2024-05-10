i = 1
while i <= 5:
    print('*' * i)
    i = i + 1       

print('done')      


print('Number Guessing Game with while Loop')   
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the secret number: "))  
    guess_count += 1                               

    if guess == secret_number:  
        print("You won!")     
        break                  
else:
    print('You failed to guess the number.')



print('Simple Car Control Simulation with while Loop')

command = ""
status = ""

while True:
    command = input("> ").lower()  

    if command == 'start':
        if status == command:
            print("Car is already started.")
        else:
            print('Car started.')
            status = command
    elif command == 'stop':
        if status == command:
            print("Car is already stopped.")
        else:
            print('Car stopped.')
            status = command
    elif command == 'help':
        print("""
              start -> to start the car
              stop -> to stop the car
              quit -> to quit
              """)
    elif command == 'quit':
        break  
    else:
        print('I don\'t understand.')  