def star(end, current, acc):
    if end < current:
        return acc
    
    mid_length = current//3
    acc = [line * 3 for line in acc] + [line + ' '*mid_length + line for line in acc] + [line * 3 for line in acc]

    return star(end, current*3, acc)


def solve():
    n = int(input())
    result = star(n, 3, ['*'])

    for line in result:
        print(line)

solve()