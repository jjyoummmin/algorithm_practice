알고리즘/자료구조 정리
=================

그래프
-----

### 경로
`오일러 경로` : 모든 edge를 한번만 방문하는 경로 (한붓그리기, 모든 정점의 차수가 짝수이면 가능)  
`해밀턴 경로` : 모든 vertex를 한번만 방문하는 경로   
`해밀턴 순환` : 한 번만 방문하여 출발지로 돌아오는 경로  
`외판원 문제 (TSP)` : 한 번만 방문하여 출발지로 돌아오는 경로 중 가장 짧은 경로  


### 그래프 순회
[DFS](dfs.md) 큐  
[BFS](bfs.md) 스택/재귀


최소비용
------

### 최단거리
네비게이션

|알고리즘| 비고 |음의 가중치|출발 노드|
|------|----|----|----|
|[dijkstras](dijkstras.md)     | bfs 사용 |x | single-source |
|[벨만포드](bellman-ford.md)     |         |ok| single-source |
|[플로이드 와샬](floydwarshall.md)|         |ok| all-source    |

* edge에 weight 없는 single-source 최단거리는 bfs로 풀수도 있음.
 


### 집합찾기
[union find](union_find.md)  


### 최소 신장 트리 (MST)
통신 네트워크 최소 비용으로 연결

[kruskal](kruskal.md) union find 사용  
[prims](prims.md)  


트리
---

정렬
---

