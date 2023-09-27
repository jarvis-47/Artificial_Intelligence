# Answer A

# Importing 'permutations' function from "itertools" module to list a state space

from itertools import permutations

# used a while loop to ensure correct user input
user_input = ''
while len(user_input) != 9:
    user_input = list(input("Please enter the puzzle piece numbers(9 digit long)"))
    if len(user_input) != 9:
        print("Entered number is not 9 digit")

# input taken for number of states to print
print_states = int(input("Please enter the desired no of states you wish to print"))

# used permutations function from itertools module to store all states as a list
all_states = list(permutations(user_input))
print("State Space - ", len(all_states))

# print the desired number of states
for i in range(0, print_states):
    a, b, c, d, e, f, g, h, i = all_states[i]
    print(a+" "+b+" "+c)
    print(d+" "+e+" "+f)
    print(g+" "+h+" "+i + "\n")
