# 바둑판 뒤집기

arr = [[int(x) for x in input().split()] for _ in range(19)]
n = int(input())
coordinate = [[int(x)-1 for x in input().split()] for _ in range(n)]


def flip(n):
    return 1 - n

def flip_arr(arr, a, b):
    for i in range(19):
        arr[a][i] = flip(arr[a][i])
        arr[i][b] = flip(arr[i][b])

def solve(arr, coordinate):
    for a, b in coordinate:
        flip_arr(arr, a, b)

    for row in arr:
        row = [str(x) for x in row]
        print(' '.join(row))


solve(arr, coordinate)