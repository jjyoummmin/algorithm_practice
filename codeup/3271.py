# 중립국 2
# 일부 테스트케이스 통과 못함...

def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x, y):
    p1, p2 = find(x), find(y)
    parent[p1] = p2


def solve():
    # 도시 그룹 계산하기
    city_count = int(input())
    global parent
    parent = [i for i in range(city_count+1)]

    edge_count = int(input())
    edges = [[int(x) for x in input().split()] for _ in range(edge_count)]

    for x, y in edges:
        union(x, y)

    # 소속 관계 (root, city)
    relation_count = int(input())
    # relations = [ (lambda x, y: [find(int(x)), int(y)] )(*input().split()) for _ in range(relation_count) ]
    relation_dict = {}
    for _ in range(relation_count):
        root, country = (lambda x, y: [find(int(x)), int(y)])(*input().split())
        relation_dict[root] = country

    
    # 결과 출력하기
    for city in range(1, city_count+1):
        root = find(city)
        print(relation_dict.get(root, 0))

  
solve()