# ANSWER B (gamma = 1, noise = 0)

# Using class defined attributes and transition model function
class mdpclass:
    def __init__(self, states, prob, discount, actions):
        self.states = states[:]
        self.prob = prob
        self.discount = discount
        self.actions = actions[:]

    # Transition model returns (probability, reward and resulting state) for a given (state, action) pair
    def transition_model(self, s, action, pr):
        q = []
        r = 0
        temp_list = []
        prp = (1 - pr) / 3
        while True:
            x, y = s
            if action == 1:
                y = y + 1
                q = [3, 4]
            elif action == 2:
                y = y - 1
                q = [3, 4]
            elif action == 3:
                x = x + 1
                q = [1, 2]
            elif action == 4:
                x = x - 1
                q = [1, 2]
            s_prime = (x, y)
            # checking for prohibited moves
            if (x < 1 or x > 3) or (y < 1 or y > 2):
                s_prime = s  # returning s' as s if move is prohibited
            temp_list.append((pr, r, s_prime))
            if pr == 1:
                return temp_list
            else:
                if not q:
                    return temp_list
                action = q.pop()
                pr = prp


# defined value iteration function printing required iterations and path of robot
def valueiteration(mdp):
    value = {}
    pi = {}

    # initializing default value +100 and -1000 for terminal states and 0 for all other states
    for state in mdp.states:
        if state == (3, 2):
            value[state] = 10
        else:
            value[state] = 0


    # function qvalue first extracts tuple triplets of (probability, reward and resulting state) from transition model
    # then returns the expected utility of a given (state, action) pair
    def qvalue(st, action, v):
        return sum(p * (r + mdp.discount * v[s_prime]) for p, r, s_prime in mdp.transition_model(st, action, mdp.prob))

    # initiated n = 100 iterations
    for i in range(1, 10):
        print("iter {}:".format(i))
        for state in mdp.states:

                # maximizing over Q value of a given (state, action) pair to assign value to the state
                value[state] = max(qvalue(state, action, value) for action in mdp.actions)

                # maximizing over Q value of a given (state, action) pair to extract policy
                pi[state] = max(((qvalue(state, action, value), action) for action in mdp.actions),
                                key=lambda tup: tup[0])
                print("state({}) V = {}     Best Action: {}".format(state, pi[state][0], pi[state][1]))



# initializing states as tuple triplets of (x, y, d) in a list
states = []
for i in range(1, 4):
    for j in range(1, 3):
            a = (i, j)
            states.append(a)


# initialize actions, noise and discount factor (gamma)
actions = [1, 2, 3, 4]
noise = 0
discount = 1

# created instance of class mdpclass
prob = 1 - noise
mdp = mdpclass(states, prob, discount, actions)

# called function for value iteration
valueiteration(mdp)
