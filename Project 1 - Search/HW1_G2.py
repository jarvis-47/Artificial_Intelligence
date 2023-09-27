# Answer G(2)
#
# Taking any arbitrary initial state for goal state - 123804765
# For instance, let initial State - 213084675
# Cost - Up: 1, Down: 1, Left: 2, Right: 0.5
# Answer -
# Path -
#  ['213084675', '013284675', '103284675', '183204675', '183274605', '183274065', '183074265', '183704265', '103784265',
#  '013784265', '713084265', '713284065', '713284605', '713204685', '713024685', '013724685', '103724685', '123704685',
#  '123784605', '123784065', '123084765', '123804765']
# No of actions taken - 32047
# Cost to Goal State -  21.5

import heapq

# defined variables

idx: int = 0
input_list = []
input_list_record = []
queue_child = []
goal_state = ['1', '2', '3', '8', '0', '4', '7', '6', '5']
counter = 0
child = []
cost = 0
parent = {}
path = []
child_string = ""
input_list_string = ""
cost_record = {}

# user input taken for puzzle piece sequence
while len(input_list) != 9:
    input_list = list(input("Please enter the puzzle piece numbers(9 digit long)"))
    if len(input_list) != 9:
        print("Entered number is not 9 digit")

# while len(goal_state) != 9:
#     goal_state = list(input("Please enter the Goal State(9 digit long)"))
#     if len(goal_state) != 9:
#         print("Entered number is not 9 digit")

u = 1  # int(input("Please enter UP Cost:"))
d = 1  # int(input("Please enter DOWN Cost:"))
r = 2  # int(input("Please enter RIGHT Cost:"))
l = 0.5  # int(input("Please enter LEFT Cost:"))

# index of directions list gives the possible actions on that index
directions = [[(1, r), (3, d)],
              [(4, d), (0, l), (2, r)],
              [(5, d), (1, l)],
              [(0, u), (4, r), (6, d)], [(1, u), (5, r), (7, d), (3, l)],
              [(2, u), (8, d), (4, l)],
              [(3, l), (7, r)],
              [(4, u), (8, r), (6, l)],
              [(5, u), (7, l)]]

# used heapq function to create priority queue
# heap function used because of within queue value swappable functionality
heapq.heapify(queue_child)
heapq.heappush(queue_child, (0, input_list))

# initiated path to capture path to goal state as per UCS
parent[("".join(map(str, input_list)))] = None
cost_record[("".join(map(str, input_list)))] = 0

# loop to continue the game until goal state is achieved
while queue_child:
    if input_list == goal_state:
        print("Input State is already Goal State!")
        break

    (cost, input_list) = heapq.heappop(queue_child)
    # Check if input node is goal state then print the required data
    if input_list == goal_state:
        input_list_record.append(input_list)
        input_list_string = "".join(map(str, input_list))
        counter += 1
        # on achieving goal state, captured the path from goal state up to the initial state
        s = input_list_string
        while s is not None:
            path.append(s)
            s = parent[s]

        print("Goal State -\n", child_string)
        sequence_string = list(map(''.join, input_list_record))
        print("Sequence -\n", sequence_string)
        print("Path -\n", path[::-1])
        print("No of actions taken -", counter)
        print("Cost to Goal State - ", cost)
        queue_child.clear()
        break
    # logic to generate UFS child node
    # check to ensure input node not in closed list
    if input_list not in input_list_record:
        input_list_record.append(input_list)
        idx = input_list.index('0')
        counter += 1
        input_list_string = "".join(map(str, input_list))
        # generating child nodes from parent node
        for i, j in directions[idx]:
            child = input_list[:]
            child[idx] = input_list[i]
            child[i] = '0'
            cost_i = cost + j
            child_string = "".join(map(str, child))

            # pushing child node to queue
            if child not in input_list_record:
                heapq.heappush(queue_child, (cost_i, child))
                heapq.heapify(queue_child)
                cost_record[child_string] = cost_i
                parent[child_string] = input_list_string
            # check if the new child node generated is already in closed list but with larger cost

            else:
                if cost_i < cost_record[child_string]:
                    # replacing the already present child node with higher cost with the new same lower cost child node
                    queue_child[queue_child.index((cost_record[child_string], child))] = (cost_i, child)
                    parent[child_string] = input_list_string
                    heapq.heapify(queue_child)
