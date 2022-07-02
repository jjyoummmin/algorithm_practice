# 막대기 놓기

h, w = [int(x) for x in input().split()]
arr = [[0] * w for _ in range(h)]
num = int(input())
bars = [[int(x) for x in input().split()] for _ in range(num)]

def put_bar(arr, bar):
    l,d,x,y = bar
    x -= 1
    y -= 1

    for i in range(l):
        if d == 0:
            arr[x][y+i] = 1
        else:
            arr[x+i][y] = 1

def print_arr(arr):
    for row in arr:
        row = [str(x) for x in row]
        print(' '.join(row))


def solve(arr, bars):
    for bar in bars:
        put_bar(arr, bar)

    print_arr(arr)
    

solve(arr, bars)  