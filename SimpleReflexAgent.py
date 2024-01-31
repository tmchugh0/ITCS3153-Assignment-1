def perceive(room_status):
        return room_status

def decide_action(room_status):
    if room_status['cleanliness']== 'dirty':
        return 'clean'
    elif room_status['obstacle']== 'yes':
        return 'avoid_obstacle'
    elif room_status['occupied']== 'yes':
        return 'wait'
    else:
        return 'move_to_next_room'

def perform_action(action):
    if action == 'clean':
        print("Clean the room")

    elif action == 'avoid_obstacle':
        print("Avoid an obstacle")
    elif action == 'wait':
        print("Waiting for the room to be unoccupied")
    elif action == 'move_to_next_room':
        print("Moving to the next room to perform cleaning")

while True:
    x = ' '
    cleanliness = input('Is the room clean or dirty? ')
    print("You chose " + cleanliness)
    print(x)
    obstacle = input('Is there an obstacle, yes or no? ')
    print("You chose " + obstacle)
    print(x)
    occupied = input('Is the room occupied, yes or no? ')
    print("You chose " + occupied)
    print(x)

    current_room_status = {'cleanliness': cleanliness, 'obstacle': obstacle,'occupied': occupied}
    action = decide_action(current_room_status)
    perform_action(action)
    perceive(current_room_status)
    print(x)
    run_again = input("Would you like to run the program again, yes or no?")
    print(x)
    if run_again == 'no':
        print("Thank you for using the Simple Reflex Agent!")

        break