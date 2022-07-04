RAOD = 0
WALL = 1
FOOD = 2
PATH = 9

def print_maze(maze):

    for row in maze:
        row = [str(x) for x in row]
        print(' '.join(row))

def move(arr, x, y):
    # 현재 위치 처리 하기
    if arr[x][y] == WALL:
        return

    elif arr[x][y] == FOOD:
        arr[x][y] = PATH
        return

    else:
        arr[x][y] = PATH

    # 이동 하기
    if arr[x][y+1] != WALL:
        move(arr, x, y+1) 
    else:
        move(arr, x+1, y)

maze = [[int(x) for x in input().split()] for _ in range(10)]
move(maze, 1, 1)
print_maze(maze)
