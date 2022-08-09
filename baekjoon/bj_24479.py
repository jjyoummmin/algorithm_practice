# == 오류 원인
# 1)
# recursion -> 딕셔너리에서 KeyError
# 반례) start vertex가 연결된 edge에 없는 경우
# 5 1 3
# 1 2
# graph = defaultdict(list) 에서 모든 vertex를 키로 가지고 있을 수 있도록 수정.

# 2
# stack -> 틀렸습니다
# 반례) cycle이 있는 그래프
# 6 7 1
# 1 6
# 1 2
# 2 6
# 2 3
# 2 4
# 3 5
# 4 5
# 넣을 때 not visited를 확인했더라도, stack에서 pop한 후 한번 더 확인해야함.

import sys
sys.setrecursionlimit(10**6)

class Dfs:
  def __init__(self):
    self.make_graph()

  def make_graph(self):
    v, e, start = map(int, sys.stdin.readline().split())
    self.v = v
    self.e = e
    self.start = start
    self.visited = [0] * (v+1)
    self.visited_order = 1

    graph = {k: [] for k in range(1, v+1)}
  
    for _ in range(e):
      a, b = map(int, sys.stdin.readline().split())
      graph[a].append(b)
      graph[b].append(a)

    graph = {k: sorted(v) for k,v in graph.items()}
    self.graph = graph

  def iter(self, node):
    pass

  def call(self):
    self.iter(self.start)
    
    for order in self.visited[1:]:
      print(order)

# stack dfs
class Stack_dfs(Dfs):
  def iter(self, start):  
    stack = [start]

    while stack:
      v = stack.pop()

      # cycle이 있는 경우 아직 stack에 있고 visited되지는 않은 노드롤 또 스택에 넣을 수 있음..
      if self.visited[v]:
        continue

      self.visited[v] = self.visited_order
      self.visited_order+=1

      for w in self.graph[v]:
        if not self.visited[w]:
          stack.append(w)


# recursion dfs
class Recursion_dfs(Dfs):  
  def iter(self, node):  
    self.visited[node] = self.visited_order
    self.visited_order += 1

    for w in self.graph[node]:
      if not self.visited[w]:
        self.iter(w)



Stack_dfs().call()
Recursion_dfs().call()