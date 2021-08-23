from typing import Any
import collections
__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = set()
        path = []
        stack = [self._root]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                stack.extend(reversed(vertex.outbound))
        return path


    def bfs(self) -> list[Node]:
        visited, queue = list(), collections.deque([self._root])
        visited.append(self._root)
        while queue:
            vertex = queue.popleft()
            for neighbour in vertex.outbound:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

