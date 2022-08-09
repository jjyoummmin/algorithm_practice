dijkstras
=========
- 최단 경로 탐색 알고리즘  
- 음의 간선 사용할 수 없음
- single source -> 모든 노드로 가는 최단 거리  
(분류)
- 다이나믹 프로그래밍 (여러 구간 최단거리를 합친 것)
- 그리디 알고리즘 (정렬 후 가장 작은 것을 먼저 선택)

#### 최초에 다익스트라 고안한 기본 알고리즘..
1. 출발 노드에서 모든 노드로 바로 가는 비용 저장
2. 방문처리 되지 않은 가장 가까운 노드부터 하나씩 고른다
3. 이 노드를 거쳐 다른 모드로 가는 비용 다시 계산 후 갱신
4. 2-3 반복

그런데 이 기본 방식은 o(n^2)이 소요되어 아주 큰 그래프에서는 비효율적이다. (2번에서 다음 방문할 가장 가까운 노드를 선형 탐색하는 경우.)  

이 대신 `BFS`를 변형한 방식으로, `priority queue`를 사용하여 다음 최단 간선을 찾아내는 방식을 알아보자 *heapq*

시간복잡도 o(e*log(v))

 
#### code
```python
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
```

* PQ에서 꺼냈을 때 이미 방문한 적이 있는 노드는 무시. (이미 방문했을 때 계산한게 가장 최단 거리이다. => 다이나믹 프로그래밍..)


