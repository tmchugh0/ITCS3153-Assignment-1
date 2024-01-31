def perceive(room_status, int_model):
    int_model['current_state'] = room_status
    int_model['history'].append(room_status)

def decide_action(int_model):
    current_state = int_model['current_state']
    history = int_model['history']
    if current_state['cleanliness']=='dirty':
        return 'clean'
    elif current_state['obstacle']=='yes':
        return 'avoid_obstacle'
    elif current_state['occupied']=='yes':
        return 'wait'
    elif len(history) > 3 and current_state['cleanliness']=='clean':
        return 'move_to_next_room'
    else:
        return 'wait'

def perform_action(action, int_model):
    current_state = int_model['current_state']
    if action =='clean':
        print("Clean the room")
    elif action == 'avoid_obstacle':
        print("Avoid an obstacle")
    elif action == 'wait':
        print("Wait for the room to be unoccupied")
    elif action == 'move_to_next_room':
        print("Move to the next room")

int_model = {'history':[], 'current_state': None}

while True:
    x = ' '


    cleanliness = input('Is the room clean or dirty? ')
    print("You chose: "+ cleanliness)
    print(x)
    obstacle = input('Is there an obstacle, yes or no? ')
    print("You chose: "+ obstacle)
    print(x)
    occupied = input('Is the room occupied, yes or no? ')
    print("You chose: "+ occupied)
    print(x)
    room_state = {'cleanliness': cleanliness, 'obstacle': obstacle, 'occupied': occupied}
    perceive(room_state, int_model)
    action = decide_action(int_model)
    perform_action(action, int_model)
    print(x)
    run_again = input('Would you like to continue cleaning, yes or no? ')
    print(x)
    if run_again == 'no':
        print("Thank you for using the Model-Based Reflex Agent! ")
        break
