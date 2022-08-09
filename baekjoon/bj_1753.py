import heapq
import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

# 입력값 받기
vertexes, edges = map(int, input().split())
start = int(input())

graph = defaultdict(list)
for _ in range(edges):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))


def dijkstra(graph, start):
  # dictionary 로 만들기...
  dist = defaultdict(int)
  pq = [(0, start)]
  
  while pq:
    cost, node = heapq.heappop(pq)

    # 이미 방문한 노드이면 무시하기 (dist에 키가 있으면 이미 방문한 것)
    if node in dist:
      continue

    dist[node] = cost
    for v, w in graph[node]:
      heapq.heappush(pq, (cost+w, v))
    
  return dist

dist = dijkstra(graph, start)
for x in range(1, vertexes+1):
  print('INF' if not x in dist else dist[x])