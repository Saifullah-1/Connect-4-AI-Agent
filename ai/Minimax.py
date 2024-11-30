from service.Service import *


class Minimax:
    def __init__(self, turn='0'):
        self.turn = turn
        self.minimax_tree = []
    
    def decision(self, state, k):
        return self.maximize(state, k)
    
    def maximize(self, state, k):
        # terminal state
        if k == 0:
            return None, eval(state)

        max_child = None
        max_utility = -float('inf')

        for child in get_children(state, self.turn):
            _, utility = self.minimize(child, k - 1)
            if utility > max_utility:
                max_utility = utility
                max_child = child

        return max_child, max_utility

    def minimize(self, state, k):
        # terminal state
        if k == 0:
            return None, eval(state)

        min_child = None
        min_utility = float('inf')

        for child in get_children(state, str(1 - int(self.turn))):
            _, utility = self.maximize(child, k - 1)
            if utility < min_utility:
                min_utility = utility
                min_child = child

        return min_child, min_utility

    def print_minimax_tree(self, state):
        # TODO -> printing the minimax tree
        pass