def print_grid():
    global grid
    
    for row in grid:
        row = [str(x) for x in row]
        print(" ".join(row))

def update_grid(x, y):
    global grid
    
    if grid[y][x] == "X":
        return
    else:
        grid[y][x] += 1

def insert_mine(x, y):
    global grid
    
    grid[y][x] = "X"
    
    # check if not out of range and not X
    
    # up
    if y - 1 >= 0:
        update_grid(x, y-1)
    
    # down
    if y + 1 < len(grid):
        update_grid(x, y+1)
    
    # left
    if x - 1 >= 0:
        update_grid(x-1, y)
    
    # right
    if x + 1 < len(grid[0]):
        update_grid(x+1, y)
    
    # up right
    if y-1 >= 0 and x + 1 < len(grid[0]):
        update_grid(x+1, y-1)
    
    # up left
    if y-1 >= 0 and x - 1 >= 0:
        update_grid(x-1, y-1)
        
    # down right
    if y + 1 < len(grid) and x + 1 < len(grid[0]):
        update_grid(x+1, y+1)
    
    # down left
    if y + 1 < len(grid) and x - 1 >= 0:
        update_grid(x-1, y+1)

width, height = [int(n) for n in input("Grid Size: ").split()]

grid = [[0 for _ in range(width)] for _ in range(height)]

n = int(input("Number of mine(s): "))
for i in range(n):
    x, y = [int(n) for n in input(f"Mine#{i+1}: ").split()]
    insert_mine(x, y)
print_grid()