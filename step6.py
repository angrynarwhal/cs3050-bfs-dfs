if __name__ == "__main__":
    import sys
    lines = sys.stdin.read().strip().split("\n")
    graph, start_node = parse_graph_from_input(lines)

    print(graph)
    print("\nBFS:")
    bfs(graph, start_node)
    print("\nDFS:")
    dfs(graph, 1)  # DFS always starts at node 1