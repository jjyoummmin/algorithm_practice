# union find 기본 문제

n, m = [int(x) for x in input().split()]
edges = [[int(x) for x in input().split()] for _ in range(m)]

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x,y):
    p1, p2 = find(x), find(y)
    p1, p2 = min(p1, p2), max(p1, p2)
    parent[p2] = p1

def solve():
    for x,y in edges:
        union(x, y)
    
    result = [str(find(x)) for x in parent][1:]
    print(' '.join(result))

solve()