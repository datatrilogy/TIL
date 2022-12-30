# Day 23_221228 수
Abstract Data Structure
```sh
Stack 
1. Last In First Out
2. 들어옴 : Push / 3. 나감 : Pop
물리적 한계에 다다르면 Stack Overflow 
node로 구성, 두가지 정보만 알고 있으면 된다.
Last : 맨 마지막에 있는 놈 / length : 실제 구현된 노드의 길이
나중에 쌓인 노드에 밑에 쌓인 노드 주소값이 표기되어 있다.
파이썬에서는 ? list.append와 pop으로 구현되어 있다. 
```
```sh
Queue : 대기줄
1. Last In Last Out == First In First Out
2 .Enqueue 먼저 들어온 놈이  / Dequeue 먼저 나간다
Double Ended Que : Pop보다 더 효율적이다(?) from collections import deque
Head / length
먼저 들어온 노드에 뒤에 들어온 노드의 주소값 표시
마찬가지로 append / pop 로 구현
```
```sh
Graph
지도, 사람과 사람사이의 관계
Node / Vertex / 정점
Edge (간선)
종류
- 서로의 관계에 따라 구분
1. 방향그래프 
2. 무방향그래프
3. 가중치그래프 : 엣지에 수치가 부여되고, 정보로써 표현됨
- CYCLE 의 유무로 구별 : 폐회로의 존재
Cycle이 없으면 Tree, 있으면 Graph
Root node, TREE 구조가 그래프 개념안에 포함됨
노드를 찾는 방법 : 깊이 들어가기 DFS / 너비 탐색 BFS (최단거리탐색)
```
```sh
그래프를 어떻게 구현할 수 있을까?
- Graph by 2d array
- Graph by Adjacency List ( 딕셔너리,인덱스)
Vertex 가 많고 Edge가 적을 때 : ADJ가 훨씬 효율적
Vertex 간의 Edge관계를 알고 싶을 때 ADJ는 순회,반복을 해야하지만, 2d array 는 그렇지 않다. 
공간은 adj list가 적게 차지하고, 시간은 2d array가 적게 걸린다.
공간 복잡도 RAM(메모리) <-> 시간 복잡도 CPU(연산량)
Big-O notation, Time complexity Chart 
O(n), O(1), O(n**2), O(logn),
Big O, Big Theta, Big Omega
```

![img](https://i0.wp.com/hanamon.kr/wp-content/uploads/2021/07/Big-O-Complexity-Chart.png?resize=1080%2C723&ssl=1)

