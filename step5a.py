import networkx as nx
import matplotlib.pyplot as plt
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

def save_graph_step(adj_list, visited, current=None, title="Graph Step", filename="step.png"):
    G = nx.Graph()
    for u in adj_list:
        for v, _ in adj_list[u]:
            G.add_edge(u, v)

    pos = nx.spring_layout(G, seed=42)  # consistent layout
    node_colors = []
    for node in G.nodes():
        if node == current:
            node_colors.append("red")          # current node
        elif node in visited:
            node_colors.append("lightblue")    # visited nodes
        else:
            node_colors.append("white")        # unvisited nodes

    plt.figure()
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edgecolors="black")
    plt.title(title)
    plt.savefig(filename)
    plt.close()

def bfs_with_save(graph, start):
    visited = set()
    distance = {start: 0}
    queue = deque([start])

    step = 1
    while queue:
        node = queue.popleft()
        save_graph_step(graph.adj_list, visited, current=node, title=f"BFS Step {step}", filename=f"bfs_step_{step}.png")
        step += 1

        for neighbor, _ in graph.adj_list.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
        visited.add(node)

def dfs_with_save(graph, start):
    visited = set()
    finish_time = {}
    time = [0]

    def dfs_visit(node, step):
        save_graph_step(graph.adj_list, visited, current=node, title=f"DFS Step {step}", filename=f"dfs_step_{step}.png")
        visited.add(node)
        for neighbor, _ in graph.adj_list.get(node, []):
            if neighbor not in visited:
                step = dfs_visit(neighbor, step + 1)
        time[0] += 1
        finish_time[node] = time[0]
        return step

    dfs_visit(start, 1)

# Example usage
if __name__ == "__main__":
    g = Graph(directed=False)
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
    for u, v in edges:
        g.add_edge(u, v)

    bfs_with_save(g, 1)
    dfs_with_save(g, 1)