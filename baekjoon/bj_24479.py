# 계속 통과 안됨.. 왜인지 모르겠음 -_-
# stack -> 틀렸습니다
# recursion -> 딕셔너리에서 KeyError

import sys
from collections import defaultdict
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

    graph = defaultdict(list)
  
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

      self.visited[v] = self.visited_order
      self.visited_order+1

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