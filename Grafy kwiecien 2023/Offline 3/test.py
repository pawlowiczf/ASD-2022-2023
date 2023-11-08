from zad6testy import runtests


from collections import deque 


from collections import deque


class HopcroftKarp:
    def __init__(self, graph):
        self.graph = graph
        self.num_left = len(graph)
        self.num_right = max(max(edges) for edges in graph.values()) + 1
        self.match_left = [-1] * self.num_left
        self.match_right = [-1] * self.num_right
        self.dist = [-1] * self.num_left
        self.inf = float('inf')

    def bfs(self):
        queue = deque()
        for left in range(self.num_left):
            if self.match_left[left] == -1:
                self.dist[left] = 0
                queue.append(left)
            else:
                self.dist[left] = self.inf

        self.dist[-1] = self.inf

        while queue:
            left = queue.popleft()

            if self.dist[left] < self.dist[-1]:
                for right in self.graph[left]:
                    if self.dist[self.match_right[right]] == self.inf:
                        self.dist[self.match_right[right]] = self.dist[left] + 1
                        queue.append(self.match_right[right])

        return self.dist[-1] != self.inf

    def dfs(self, left):
        if left == -1:
            return True

        for right in self.graph[left]:
            if self.dist[self.match_right[right]] == self.dist[left] + 1 and self.dfs(self.match_right[right]):
                self.match_left[left] = right
                self.match_right[right] = left
                return True

        self.dist[left] = self.inf
        return False

    def max_matching(self):
        matching = 0

        while self.bfs():
            for left in range(self.num_left):
                if self.match_left[left] == -1 and self.dfs(left):
                    matching += 1

        return matching


def binworker( M ):
    return HopcroftKarp.max_matching(M)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )
