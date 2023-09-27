# ANSWER D (gamma = 0.8, noise = 0)

# Using class defined attributes and transition model function
class mdpclass:
    def __init__(self, states, prob, discount, actions):
        self.states = states[:]
        self.prob = prob
        self.discount = discount
        self.actions = actions[:]

    # Transition model returns (probability, reward and resulting state) for a given (state, action) pair
    def transition_model(self, s, action, pr):
        q = [1, 2, 3, 4]
        r = 0
        temp_list = []
        prp = (1 - pr) / 3
        q.remove(action)
        while True:
            x, y, z = s
            if action == 1:
                r = -1.5
                if s[2] == 1:
                    y = y + 1
                elif s[2] == 2:
                    y = y - 1
                elif s[2] == 3:
                    x = x - 1
                elif s[2] == 4:
                    x = x + 1
            elif action == 2:
                r = -2
                if s[2] == 1:
                    y = y + 2
                elif s[2] == 2:
                    y = y - 2
                elif s[2] == 3:
                    x = x - 2
                elif s[2] == 4:
                    x = x + 2
            elif action == 3:
                r = -0.5
                if s[2] == 1:
                    z = z + 2
                elif s[2] == 2:
                    z = z + 2
                elif s[2] == 3:
                    z = z - 1
                elif s[2] == 4:
                    z = z - 3
            elif action == 4:
                r = -0.5
                if s[2] == 1:
                    z = z + 3
                elif s[2] == 2:
                    z = z + 1
                elif s[2] == 3:
                    z = z - 2
                elif s[2] == 4:
                    z = z - 2
            s_prime = (x, y, z)
            # checking for prohibited moves
            if (x < 1 or x > 5) or (y < 1 or y > 5) or \
                    (s[:2] in [(2, 2), (2, 3), (3, 2)] or s_prime[:2] in [(2, 2), (2, 3), (3, 2)]) or \
                    (s[:2] in [(2, 5), (5, 3)] and s_prime[:2] in [(3, 5), (4, 5), (5, 4), (5, 5)]) or \
                    (s[:2] in [(1, 5), (5, 2)] and s_prime[:2] in [(3, 5), (5, 4)]) or \
                    (s[:2] in [(3, 5), (5, 4)] and s_prime[:2] in [(1, 5), (2, 5), (5, 2), (5, 3)]) or \
                    (s[:2] in [(4, 5)] and s_prime[:2] in [(2, 5)]) or \
                    (s[:2] in [(4, 3), (3, 4)] and s_prime[:2] in [(5, 4), (4, 5)]) or \
                    (s[:2] in [(5, 4), (4, 5)] and s_prime[:2] in [(4, 3), (3, 4)]) or \
                    (s[:2] in [(3, 1), (1, 3)] and s_prime[:2] in [(3, 3)]) or \
                    (s[:2] in [(3, 3)] and s_prime[:2] in [(3, 1), (1, 3)]):
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
        if state[:2] == (5, 5):
            value[state] = 100.
            pi[state] = None
        elif state[:2] == (4, 4):
            value[state] = -1000.
            pi[state] = None
        else:
            value[state] = 0.

    # function qvalue first extracts tuple triplets of (probability, reward and resulting state) from transition model
    # then returns the expected utility of a given (state, action) pair
    def qvalue(st, action, v):
        return sum(p * (r + mdp.discount * v[s_prime]) for p, r, s_prime in mdp.transition_model(st, action, mdp.prob))

    # initiated n = 100 iterations
    for i in range(1, 101):
        if i < 11:
            print("iter {}:".format(i))
        for state in mdp.states:
            if state[:2] not in [(4, 4), (5, 5), (3, 2), (2, 2), (2, 3)]:

                # maximizing over Q value of a given (state, action) pair to assign value to the state
                value[state] = max(qvalue(state, action, value) for action in mdp.actions)

                # maximizing over Q value of a given (state, action) pair to extract policy
                pi[state] = max(((qvalue(state, action, value), action) for action in mdp.actions),
                                key=lambda tup: tup[0])
                if i < 11:
                    print("state({}) V = {}     Best Action: {}".format(state, pi[state][0], pi[state][1]))

    s = (1, 1, 4)  # initial state of robot
    result = []  # list to capture the resulting best path of robot to end state
    while pi[s] is not None:
        q, act = pi[s]  # extracting best action for a state from already extracted policy over 100 iterations

        # extracting next state from best action for a given state
        j_list = mdp.transition_model(s, act, 1)
        x, y, z = j_list[0]

        result.append((s, pi[s]))
        s = z

    result.append((s, pi[s]))
    print("Result:", result)



# initializing states as tuple triplets of (x, y, d) in a list
states = []
for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 5):
            a = (i, j, k)
            states.append(a)


# initialize actions, noise and discount factor (gamma)
actions = [1, 2, 3, 4]
noise = 0
discount = 0.8

# created instance of class mdpclass
prob = 1 - noise
mdp = mdpclass(states, prob, discount, actions)

# called function for value iteration
valueiteration(mdp)
