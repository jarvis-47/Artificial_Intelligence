# Answer C

import random

# defined variables
user_input = ''
input_list = []
record = []
action_count = []
t = True
counter = 0

# index of directions list gives the possible actions on that index
directions = [[(1, 'right'), (3, 'down')],
              [(4, 'down'), (0, 'left'), (2, 'right')],
              [(5, 'down'), (1, 'left')],
              [(0, 'up'), (4, 'right'), (6, 'down')], [(1, 'up'), (5, 'right'), (7, 'down'), (3, 'left')],
              [(2, 'up'), (8, 'down'), (4, 'left')],
              [(3, 'left'), (7, 'right')],
              [(4, 'up'), (8, 'right'), (6, 'left')],
              [(5, 'up'), (7, 'left')]]

# user input taken for puzzle piece sequence
while len(user_input) != 9:
    user_input = input("Please enter the puzzle piece numbers(9 digit long)")
    if len(user_input) != 9:
        print("Entered number is not 9 digit")

# converted input to int list
input_list = [int(i) for i in user_input]

# initiated record for sequence of state, action
record.append((input_list, "initial"))

# loop to continue the game until goal state is achieved
while t:
    if sum(input_list[0:3]) % 3 == 0 and sum(input_list[3:6]) % 3 == 0 and sum(input_list[6:9]) % 3 == 0:
        print("Input State is already Goal State!")
        break
# logic to generate child node
    idx = input_list.index(0)
    i, action = random.choice(directions[idx])
    child = input_list[:]
    child[idx] = input_list[i]
    child[i] = 0
    input_list = child[:]
    record.append((input_list, action))
    counter += 1
    # Check if child node is goal state then print the required data
    if sum(input_list[0:3]) % 3 == 0 and sum(input_list[3:6]) % 3 == 0 and sum(input_list[6:9]) % 3 == 0:
        print("Goal State -\n", input_list)
        print("Sequence of states -\n", record)
        print("No of actions taken -\n", counter)
        t = False
        break
