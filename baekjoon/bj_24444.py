# BFS 기본문제
# 입력때문에 타임아웃 : sys.stdin.readline 사용할 것

import sys
from collections import defaultdict, deque

def make_graph():
  v, e, start = map(int, sys.stdin.readline().split())
  graph = defaultdict(list)
  
  for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

  graph = {k: sorted(v) for k,v in graph.items()}

  return v, graph, start

def bfs(v, graph, start):
  visited = [0] * (v+1)
  queue = deque([start])
  visited[start] = 1

  visited_order = 2

  while queue:
    v = queue.popleft()
    for w in graph[v]:
      if visited[w]:
        continue
      queue.append(w)
      visited[w] = visited_order
      visited_order += 1
  
  return visited[1:]




def solve():
  v, graph, start = make_graph()
  visited = bfs(v, graph, start)

  for order in visited:
    print(order)

solve()