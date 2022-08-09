BFS
===
- 넓이 우선 탐색 (같은 level인 순서로 탐색)
- `큐` 사용해서 구현
- *최단 거리 찾기 (간선에 weight가 없는 경우)*, *미로 찾기* 등에서 사용

1) 큐에서 노드 하나 꺼내기
2) 꺼낸 노드 인접한 방문하지 않은 노드 큐에 삽입 (하면서 방문처리)

   
큐, 방문여부 array 2가지 필요


```python
def bfs(start):
  visited = [False] * (v+1)
  queue = deque([start])
  visited[start] = True

  while queue:
    # 큐에서 노드 하나 꺼내기
    v = queue.popleft()
    # v의 모든 인접노드 w
    for w in graph[v]:
      if visited[w]:
        continue
      queue.append(w)
      visited[w] = True
  
  return visited[1:]
```

visited에 boolean대신 방문 순서를 저장할 수도 있음.