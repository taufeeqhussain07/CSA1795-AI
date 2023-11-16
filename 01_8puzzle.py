import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def heuristic(self):
        # Manhattan distance heuristic
        total_distance = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_i, goal_j = divmod(self.state[i][j] - 1, 3)
                    total_distance += abs(i - goal_i) + abs(j - goal_j)

        return total_distance

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(node):
    i, j = get_blank_position(node.state)
    neighbors = []

    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + move[0], j + move[1]
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in node.state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, parent=node, move=(ni, nj), depth=node.depth + 1, cost=node.depth + 1))

    return neighbors

def a_star(initial_state):
    initial_node = PuzzleNode(initial_state)
    goal_state = [[1, 0, 3], [4, 2, 6], [7, 5, 8]]

    if initial_state == goal_state:
        return [initial_state]

    frontier = [initial_node]
    explored = set()

    while frontier:
        current_node = heapq.heappop(frontier)
        explored.add(current_node)

        for neighbor in get_neighbors(current_node):
            if neighbor.state == goal_state:
                # Reconstruct the path
                path = [neighbor.state]
                while neighbor.parent:
                    path.insert(0, neighbor.parent.state)
                    neighbor = neighbor.parent
                return path

            if neighbor not in explored and neighbor not in frontier:
                heapq.heappush(frontier, neighbor)

    return None

def print_puzzle(state):
    for row in state:
        print(row)
    print()

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solution = a_star(initial_state)

    if solution:
        print("Solution found!")
        for step, state in enumerate(solution):
            print(f"Step {step + 1}:")
            print_puzzle(state)
    else:
        print("No solution found.")
