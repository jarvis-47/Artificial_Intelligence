# Answer E

# No of actions taken -
# 172692

# defined variables
input_list = []
idx: int = 0
queue_list: list = []
goal_state = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
record = []
record_temp = []
counter = 0

# index of directions list gives the possible actions on that index
directions = [[1, 3], [4, 0, 2], [5, 1], [0, 4, 6], [1, 5, 7, 3], [2, 8, 4], [3, 7], [4, 8, 6], [5, 7]]

# user input taken for puzzle piece sequence
while len(input_list) != 9:
    input_list = list(input("Please enter the puzzle piece numbers(9 digit long)"))
    if len(input_list) != 9:
        print("Entered number is not 9 digit")

# initiated queue for DFS
queue_list.append(input_list)

# loop to continue the game until goal state is achieved
while True:
    if input_list == goal_state:
        print("Input State is already Goal State!")
        break
    # logic to generate DFS child node
    input_list = queue_list.pop()
    if input_list not in record_temp:
        record_temp.append(input_list)
        idx = input_list.index('0')
        for i in directions[idx]:
            test = input_list[:]
            test[idx] = test[i]
            test[i] = '0'
            queue_list.append(test)
    # initiated sequence record of visited states
        record.append("".join(map(str, input_list)))
        counter += 1
        # Check if child node is goal state then print the required data
        if input_list == goal_state:
            print("Sequence -\n" + f'{record}')
            print("Goal State -\n" + f'{input_list}')
            print("No of actions taken -\n" + f'{counter}')
            break
