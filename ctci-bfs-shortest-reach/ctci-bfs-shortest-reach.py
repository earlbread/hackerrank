from collections import defaultdict

default_length = 6

class Graph:

    def __init__(self, size):
        self.size = size
        self.edges = defaultdict(lambda: [])

    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, start):
        distances = [-1 for _ in range(self.size)]
        distances[start] = 0

        q = [start]

        while len(q) != 0:
            node = q.pop(0)

            for neighbor in self.edges[node]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[node] + default_length
                    q.append(neighbor)
        return distances


t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    distances = graph.find_all_distances(s-1)
    print(' '.join(
        map(str, [distance for distance in distances if distance != 0])))
