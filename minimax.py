from copy import deepcopy

X = "X"
O = "O"
N = None


class Game:
    def __init__(self):
        self.current_state = [[N, N, N], [N, N, N], [N, N, N]]
        self.player = X

    def get_state(self):
        return self.current_state

    def apply_move(self, action):
        """
        take an action and change the player from X to O and vice versa
        """
        row, col = action
        self.current_state[row][col] = self.player
        if self.player == X:
            self.player = O
        else:
            self.player = X

    def to_move(self):
        """
        returns which player will move next
        """
        return self.player

    def actions(self, state):
        """
        returns the set of legal actions
        """
        actions = []
        for r, row in enumerate(state):
            for c, value in enumerate(row):
                if value is None:
                    actions.append((r, c))
        return actions

    def result(self, state, action, player):
        """
        returns the next state that results from the (state, action) pair
        """
        r, c = action
        new_state = deepcopy(state)
        new_state[r][c] = player
        return new_state

    def is_terminal(self, state):
        """
        returns a boolian indicating if the game has reached a terminal state
        """
        # check if someone one
        for i in range(3):
            # rows
            if state[i][0] == state[i][1] == state[i][2] != None:
                return True
            # cols
            if state[0][i] == state[1][i] == state[2][i] != None:
                return True
            # diagonal
            if state[0][0] == state[1][1] == state[2][2] != None:
                return True
            # opposing diagonal
            if state[2][0] == state[1][1] == state[0][2] != None:
                return True

        # check if there are empty cells
        for row in state:
            for value in row:
                if value is None:
                    return False

        return True

    def utility(self, state):
        """
        returns the utility for player for the terminal state
        """
        for i in range(3):
            # rows
            if state[i][0] == state[i][1] == state[i][2]:
                if state[i][0] == X:
                    return 1
                if state[i][0] == O:
                    return -1

            # cols
            if state[0][i] == state[1][i] == state[2][i]:
                if state[0][i] == X:
                    return 1
                if state[0][i] == O:
                    return -1

            # diagonal
            if state[0][0] == state[1][1] == state[2][2]:
                if state[0][0] == X:
                    return 1
                if state[0][0] == O:
                    return -1
                return True
            # opposing diagonal
            if state[2][0] == state[1][1] == state[0][2]:
                if state[2][0] == X:
                    return 1
                if state[2][0] == O:
                    return -1
        return 0

    def minimiax(self, state):
        """
        returns the optimal action
        """
        move = None
        if self.player == X:
            _, move = self.max_value(state)
        if self.player == O:
            _, move = self.min_value(state)
        return move

    def max_value(self, state):
        player = X
        if self.is_terminal(state):
            return self.utility(state), None
        v = float("-inf")
        move = None
        for a in self.actions(state):
            v2, _ = self.min_value(self.result(state, a, player))
            if v2 > v:
                v, move = v2, a
        return v, move

    def min_value(self, state):
        player = O
        if self.is_terminal(state):
            return self.utility(state), None
        v = float("+inf")
        move = None
        for a in self.actions(state):
            v2, _ = self.max_value(self.result(state, a, player))
            if v2 < v:
                v, move = v2, a
        return v, move

    def make_move(self, action=None):
        state = self.get_state()

        # only use minimax for the computer
        if action is None:
            action = self.minimiax(state)

        # make sure the move is legal
        if action in self.actions(state):
            self.apply_move(action)


if __name__ == "__main__":
    # for debugging purposes
    game = Game()
