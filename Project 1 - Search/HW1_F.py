# Answer F

# For a given goal state, there are only 9!/2 initial states possible to reach that goal state.
# For the given initial state in part (F) - 724506831, the required goal state - 123804765 is not achievable
# Hence, some other arbitrary initial state may result in the required goal state,
# but the initial state given in question cannot yield the required goal state

import queue


# defined variables

idx: int = 0
input_list = []
input_list_record = []
queue_child = queue.Queue()
goal_state = []
record = []
counter = 0
child = []
record_print = []


# index of directions list gives the possible actions on that index
directions = [[1, 3], [4, 0, 2], [5, 1], [0, 4, 6], [1, 5, 7, 3], [2, 8, 4], [3, 7], [4, 8, 6], [5, 7]]

# user input taken for puzzle piece sequence
while len(input_list) != 9:
    input_list = list(input("Please enter the puzzle piece numbers(9 digit long)"))
    if len(input_list) != 9:
        print("Entered number is not 9 digit")
# user input taken for goal state sequence
while len(goal_state) != 9:
    goal_state = list(input("Please enter the Goal State(9 digit long)"))
    if len(goal_state) != 9:
        print("Entered number is not 9 digit")

queue_child.put(input_list)
record.append(input_list)

while not queue_child.empty():
    if input_list == goal_state:
        print("Input State is already Goal State!")
        break

    input_list = queue_child.get()
    if input_list not in input_list_record:
        input_list_record.append(input_list)
        idx = input_list.index('0')
        for i in directions[idx]:
            child = input_list[:]
            child[idx] = input_list[i]
            child[i] = '0'
            if child not in record:
                queue_child.put(child)
                record.append(child)
                record_print.append(''.join(map(str, child)))
                counter += 1
            if child == goal_state:
                print("Goal State -\n", child)
                print("Sequence -\n", record_print)
                print("No of actions taken -\n", counter)
                queue_child.queue.clear()
                break


