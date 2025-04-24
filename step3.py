from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append((v, weight))
        if not self.directed:
            if v not in self.adj_list:
                self.adj_list[v] = []
            self.adj_list[v].append((u, weight))

    def __str__(self):
        out = ["Graph (Directed)" if self.directed else "Graph (Undirected)"]
        for u in sorted(self.adj_list):
            edges = ", ".join([f"{u}->{v} ({w})" for v, w in self.adj_list[u]])
            out.append(f"{edges}")
        return "\n".join(out)

def bfs(graph, start):
    visited = set()
    distance = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(f"{node}({distance[node]})", end=" ")

        for neighbor, _ in graph.adj_list.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
        
        visited.add(node)
    print()  # newline for clean output

"""
        1 -- 2
        |     \
        3      4 -- 5
        \____/

"""

def dfs(graph, start):
    visited = set()
    finish_time = {}
    time = [0]  # Mutable object to track time

    def dfs_visit(node):
        visited.add(node)
        for neighbor, _ in graph.adj_list.get(node, []):
            if neighbor not in visited:
                dfs_visit(neighbor)
        time[0] += 1
        finish_time[node] = time[0]

    # Start DFS from node 1 if unspecified
    dfs_visit(start)

    # Output: sort nodes by finish time descending (like in the example)
    for node, f_time in sorted(finish_time.items(), key=lambda x: -x[1]):
        print(f"{node}({f_time})", end=" ")
    print()
    
if __name__ == "__main__":
    g = Graph(directed=False)

    # Define the same graph structure
    g.add_edge(1, 2, 1.0)
    g.add_edge(1, 3, 1.0)
    g.add_edge(2, 4, 1.0)
    g.add_edge(3, 4, 1.0)
    g.add_edge(4, 5, 1.0)

    print(g)
    
    # BFS Demonstration
    print("\nBFS from node 1:")
    bfs(g, 3)

    # DFS Demonstration
    print("\nDFS from node 1:")
    dfs(g, 3)