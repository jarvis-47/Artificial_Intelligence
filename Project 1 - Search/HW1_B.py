# Answer B

# taking the current state and action from user to return the output state

# defined variables
input_list = []
action_input = 0
blank_spot_idx = 0

# user input taken for puzzle piece sequence
while len(input_list) != 9:
    input_list = list(input("Please enter the puzzle piece numbers(9 digit long)"))
    if len(input_list) != 9:
        print("Entered number is not 9 digit")

# identified the index position of '0' in input state list
blank_spot_idx = input_list.index("0")

# action input taken from user while simultaneously filtered invalid entries
while action_input not in range(1, 5):
    action_input = int(input("Please enter the action for 'blank spot'\n Please note: \n moving up:1\n down:2 "
                             "\n left:3\n right:4 \n Action - "))
    if action_input not in range(1, 5):
        print("Invalid Entry! Please enter correct value")
    elif blank_spot_idx in [0, 1, 2]:
        if action_input == 1:
            print("Restricted Movement!!")
            action_input = 0
    elif blank_spot_idx in [0, 3, 6]:
        if action_input == 3:
            print("Restricted Movement!!")
            action_input = 0
    elif blank_spot_idx in [2, 5, 8]:
        if action_input == 4:
            print("Restricted Movement!!")
            action_input = 0
    elif blank_spot_idx in [6, 7, 8]:
        if action_input == 2:
            print("Restricted Movement!!")
            action_input = 0

# action from current state to output state taken
if action_input == 1:
    input_list[blank_spot_idx] = input_list[blank_spot_idx - 3]
    input_list[blank_spot_idx - 3] = 0
elif action_input == 2:
    input_list[blank_spot_idx] = input_list[blank_spot_idx + 3]
    input_list[blank_spot_idx + 3] = 0
elif action_input == 3:
    input_list[blank_spot_idx] = input_list[blank_spot_idx - 1]
    input_list[blank_spot_idx - 1] = 0
else:
    input_list[blank_spot_idx] = input_list[blank_spot_idx + 1]
    input_list[blank_spot_idx + 1] = 0

# print output
print("Output State -\n" + f'{"".join(map(str, input_list))}')
