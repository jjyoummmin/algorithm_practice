import sys
from collections import defaultdict

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
    self.visited[node] = self.visited_order
    self.visited_order += 1

    for w in self.graph[node]:
      if not self.visited[w]:
        self.iter(w)

  def call(self):
    self.iter(self.start)
    
    for order in self.visited[1:]:
      print(order)


Dfs().call()



