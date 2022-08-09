DFS
===
- 깊이 우선 탐색
- 스택 / 재귀 사용해서 구현

방문 여부를 저장할 수 있는 배열이 필요하다.

스택
---
```python
def dfs(start):  
  stack = [start]

  while stack:
    v = stack.pop()

    # cycle이 있는 경우 때문에 확인필요
    if visited[v]:
      continue

    visited[v] = True

    for w in graph[v]:
      if not visited[w]:
        stack.append(w)

  return visited
```

재귀
---
현재 노드를 방문 처리하고, 모든 인접노드에 대해 dfs를 수행한다.
```python
def dfs(node):  
  visited[node] = True

  for w in graph[node]:
    if not visited[w]:
      dfs(w)
```

