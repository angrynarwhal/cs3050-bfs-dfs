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

