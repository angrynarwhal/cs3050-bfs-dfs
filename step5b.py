import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        self.adj_list = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append((v, weight))
        if v not in self.adj_list:
            self.adj_list[v] = []

    @staticmethod
    def from_file(file_path):
        graph = Graph(directed=True)
        with open(file_path, 'r') as f:
            for line in f:
                u, v, w = map(float, line.strip().split())
                graph.add_edge(int(u), int(v), w)
        return graph

def save_graph_step(adj_list, distances, current=None, title="Graph Step", filename="step.png"):
    G = nx.DiGraph()
    for u in adj_list:
        for v, w in adj_list[u]:
            G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)
    node_labels = {node: f"{node}\n{distances.get(node, '∞')}" for node in G.nodes()}
    edge_labels = nx.get_edge_attributes(G, 'weight')
    node_colors = []
    for node in G.nodes():
        if node == current:
            node_colors.append("red")
        elif node in distances and distances[node] < float('inf'):
            node_colors.append("lightblue")
        else:
            node_colors.append("white")

    plt.figure()
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_color=node_colors, edgecolors="black")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.savefig(filename)
    plt.close()

def bellman_ford_with_save(graph, start):
    distances = {node: float('inf') for node in graph.adj_list}
    distances[start] = 0
    step = 1

    for _ in range(len(graph.adj_list) - 1):
        updated = False
        for u in graph.adj_list:
            for v, w in graph.adj_list[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    updated = True
        save_graph_step(graph.adj_list, distances, current=None, title=f"Relaxation Step {step}", filename=f"relax_step_{step}.png")
        step += 1
        if not updated:
            break

# Example usage
if __name__ == "__main__":
    input_file = "graph_input.txt"
    g = Graph.from_file(input_file)
    bellman_ford_with_save(g, start=1)