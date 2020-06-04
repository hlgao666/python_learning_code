car_condition = 'stop'
end_str = 'quit'

while True:

    command = input('> ').lower()

    if car_condition == command:
        if car_condition == 'stop':
            print('Car is already stopped. Plz try other commands!')
        else:
            print('Car is already started. Plz try other commands!')
        continue

    if command.lower() == 'help':
        print('''start-to start the car
stop-to stop the car
quit-to exit''')
    elif command == 'start':
        car_condition = command
        print('Car started. Ready to go.')
    elif command == 'stop':
        car_condition = command
        print('Car stopped')
    elif command == end_str:
        break
    else:
        print('sorry, I don\'t understand that...')
