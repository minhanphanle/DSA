import queue
MAX = 100
INF = int(1e9)


graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]

# O(ElogV)


class Node:
    def __init__(self, _id, _weight):
        self.id = _id
        self.weight = _weight

    # Define the less-than method to compare nodes based on weight
    # used for priority queue
    def __lt__(self, other):
        return self.weight < other.weight


def Dijkstra(exit_index):
    pq = queue.PriorityQueue()
    pq.put(Node(exit_index, 0))

    dist[exit_index] = 0

    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.weight

        for n in graph[u]:
            if n.weight + w < dist[n.id]:
                dist[n.id] = n.weight + w
                pq.put(Node(n.id, dist[n.id]))


N = int(input())
E = int(input())
T = int(input())
M = int(input())

for _ in range(M):
    u, v, w = map(int, input().split())
    # directed graph, reverse the graph to run Dijktra from the end vertex to all other vertices
    graph[v].append(Node(u, w))

Dijkstra(E)

count = 0

for i in range(1, N+1):
    if dist[i] <= T:
        count += 1

print(count)
