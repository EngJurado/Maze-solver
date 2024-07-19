import heapq

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for d in directions:
        nx, ny = node[0] + d[0], node[1] + d[1]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
            neighbors.append((nx, ny))
    return neighbors

def a_star_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + manhattan_distance(start, goal), 0, "", start))
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, cost, _, current = heapq.heappop(open_set)
        
        if current == goal:
            current = came_from[current]  # Start backtracking from the parent of the goal
            while current in came_from:
                grid[current[0]][current[1]] = 5
                current = came_from[current]
            return grid
        
        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g_score, id(neighbor), neighbor))
    
    return grid

# Define the map
map = [
    [2, 0, 0, 1, 1, 0, 0, 0, 3, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Find start and goal positions
start = next((x, y) for x, row in enumerate(map) for y, val in enumerate(row) if val == 2)
goal = next((x, y) for x, row in enumerate(map) for y, val in enumerate(row) if val == 3)

# Run A* search
solution_map = a_star_search(map, start, goal)

# Print the solution map
print(solution_map)