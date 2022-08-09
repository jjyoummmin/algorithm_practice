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

    graph = {k: [] for k in range(1, v+1)}
  
    for _ in range(e):
      a, b = map(int, sys.stdin.readline().split())
      graph[a].append(b)
      graph[b].append(a)

    graph = {k: sorted(v, reverse=True) for k,v in graph.items()}
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

Stack_dfs().call()