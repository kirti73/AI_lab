class EightPuzzleDFS:
    def __init__(self, initial_state, goal_state):
        self.initial_state = tuple(initial_state)
        self.goal_state = tuple(goal_state)
        self.moves = {
            'UP': (-1, 0),
            'DOWN': (1, 0),
            'LEFT': (0, -1),
            'RIGHT': (0, 1)
        }

    def find_blank(self, state):
        # 0 represents the empty space
        idx = state.index(0)
        return idx // 3, idx % 3

    def get_neighbors(self, state):
        neighbors = []
        r, c = self.find_blank(state)
        for move, (dr, dc) in self.moves.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = list(state)
                idx1 = r * 3 + c
                idx2 = nr * 3 + nc
                new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
                neighbors.append(tuple(new_state))
        return neighbors

    def solve(self):
        stack = [(self.initial_state, [self.initial_state])]
        visited = {self.initial_state}

        while stack:
            current_state, path = stack.pop()

            if current_state == self.goal_state:
                return path

            for neighbor in self.get_neighbors(current_state):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))
        return None

    def print_board(self, state):
        for i in range(0, 9, 3):
            print(f"{state[i]} {state[i+1]} {state[i+2]}")
        print()
