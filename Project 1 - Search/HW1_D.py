# Answer D

# To reach goal state - 012345678 from initial state - 724506831 using BFS:
# No of actions taken - 173341

import queue

# defined variables

idx: int = 0
input_list = []
input_list_record = []
queue_child = queue.Queue()
goal_state = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
record = []
counter = 0
child = []
record_print = []

# index of directions list gives the possible actions on that index
directions = [[1, 3], [4, 0, 2], [5, 1], [0, 4, 6], [1, 5, 7, 3], [2, 8, 4], [3, 7], [4, 8, 6], [5, 7]]

# if user input required for puzzle piece sequence
while len(input_list) != 9:
    input_list = list(input("Please enter the puzzle piece numbers(9 digit long)"))
    if len(input_list) != 9:
        print("Entered number is not 9 digit")

# initiated queue for BFS
queue_child.put(input_list)
# initiated sequence record of visited states
record.append(input_list)

# loop to continue the game until goal state is achieved
while not queue_child.empty():
    if input_list == goal_state:
        print("Input State is already Goal State!")
        break
    # logic to generate BFS child node
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
                print(counter)
            # Check if child node is goal state then print the required data
            if child == goal_state:
                print("Goal State -\n", child)
                print("Sequence -\n", record_print)
                print("No of actions taken -\n", counter)
                queue_child.queue.clear()
                break


