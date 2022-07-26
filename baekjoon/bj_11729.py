# (hanoi(n-1)의 목적지를 3->2로 수정)
# 2 <-> 3
def pre_transform(n):
    return 2 if n==3 else (3 if n==2 else n)

# (hanoi(n-1)의 출발지를 1->2로 수정)
# 1 <-> 2
def post_transform(n):
    return 1 if n==2 else (2 if n==1 else n)

def hanoi(end, n, acc):
    if n > end:
        print(len(acc))
        for x,y in acc:
            print(x, y)
        return
    
    acc = [(pre_transform(x), pre_transform(y)) for x, y in acc] + [(1, 3)] + [(post_transform(x), post_transform(y)) for x, y in acc]
    hanoi(end, n+1, acc)

size = int(input())
hanoi(size, 1, [])