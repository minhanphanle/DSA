import queue
MAX = 505
INF = int(1e9)

# use index in a two-dimensional array instead
# of key-value dict with value as list
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]


class Node:
    def __init__(self, _id, _weight):
        self.id = _id
        self.weight = _weight

    def __lt__(self, other):
        return self.weight < other.weight


def Dijkstra(index):
    pq = queue.PriorityQueue()
    pq.put(Node(index, 0))
    dist[index] = 0

    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.weight

        for neighbor in graph[u]:
            # if new dist (weight + dist of prev) is less than curr dist
            if neighbor.weight + w < dist[neighbor.id]:
                # update dist
                dist[neighbor.id] = neighbor.weight + w
                pq.put(Node(neighbor.id, dist[neighbor.id]))


N = int(input())
for _ in range(N):
    A, B, W = map(int, input().split())
    graph[A].append(Node(B, W))
    graph[B].append(Node(A, W))

start_vertex = int(input())
Dijkstra(start_vertex)

Q = int(input())
for _ in range(Q):
    V = int(input())
    print(dist[V] if dist[V] != INF else "NO PATH")
