import heapq
# Function to find the position of the blank (0)
def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

# Function to generate all possible successor states
def successors(puzzle):
    successors = []
    i, j = find_blank(puzzle)
    for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        new_i, new_j = i + move[0], j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[i][j], new_puzzle[new_i][new_j] = new_puzzle[new_i][new_j], new_puzzle[i][j]
            successors.append(new_puzzle)
    return successors

# Heuristic function: Misplaced tiles
def misplaced_tiles(puzzle):
    count = 0
    g=[[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != g[i][j]:
                count += 1
    return count

# Heuristic function: Manhattan distance
def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = puzzle[i][j]
            if value != 0:
                target_row = value // 3
                target_col = value % 3
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

# A* algorithm
def astar(initial_state, heuristic_func):
    c=0
    frontier = []
    heapq.heappush(frontier, (heuristic_func(initial_state), c, initial_state, []))  # Store the path as well
    visited = set()
    while frontier:
        _, c, state, path = heapq.heappop(frontier)
        if state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return path + [state]  # Return the path taken to reach the goal state
        visited.add(tuple(map(tuple, state)))
        for successor in successors(state):
            if tuple(map(tuple, successor)) not in visited:
                heapq.heappush(frontier, (heuristic_func(successor) + c + 1, c + 1, successor, path + [state]))
    return 0
# Test the algorithm
initial_state = [[1, 2, 3], [4, 5, 6], [ 8,7,0]]

print("Initial state:")
for row in initial_state:
    print(row)

print("\nA* Algorithm using Misplaced Tiles Heuristic:")
solution_misplaced_tiles = astar(initial_state, misplaced_tiles)
if solution_misplaced_tiles==0:
    print("No solution possible")
else:
    print("Solution using Misplaced Tiles Heuristic:")
    for state in solution_misplaced_tiles:
        for row in state:
            print(row)
        print()
    print("has", len(solution_misplaced_tiles) - 1, "moves")

print("\nA* Algorithm using Manhattan Distance Heuristic:")
solution_manhattan_distance = astar(initial_state, manhattan_distance)
if solution_manhattan_distance==0:
    print("No solution possible")
else:
    print("Solution using Manhattan Distance Heuristic:")
    for state in solution_manhattan_distance:
        for row in state:
            print(row)
        print()
    print("has", len(solution_manhattan_distance) - 1, "moves")
