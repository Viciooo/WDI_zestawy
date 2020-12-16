
grid = [[5,0,0,0,8,0,0,4,9],
[0,0,0,5,0,0,0,3,0],
[0,6,7,3,0,0,0,0,1],
[1,5,0,0,0,0,0,0,0],
[0,0,0,2,0,8,0,0,0],
[0,0,0,0,0,0,0,1,8],
[7,0,0,0,0,4,1,5,0],
[0,3,0,0,0,2,0,0,0],
[4,9,0,0,5,0,0,0,3]]

def possible(y, x, n):
    global grid
    for i in range(9):
        if grid[y][i] == n or grid[i][x] == n:
            return False
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    for i in grid:
        print(i)
    input("More?")

solve()