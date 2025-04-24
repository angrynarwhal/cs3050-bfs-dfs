# cs3050-bfs-dfs
Pythonic Example of breadth first and depth first search

## Setting up Environment: 
- The first several programs do not require any libraries. 
- Step 6 is the first step that requires a python environment because of two libraries. Before that step: 
    - `python3 -m venv .venv`
    - `source .venv/bin/activate`
    - `pip install -r requirements.txt`

# Conceptual Steps Followed by the Programs (Maybe not perfectly; These are Pre-Code Notes): 
1.	Step-by-step buildup:
 - Start with graph construction from the provided input format.
 - Visualize simple graph examples to introduce nodes and edges.
 - Implement BFS, showing node discovery order and distances.
 - Implement DFS, showing discovery and finish times.
 - Apply both algorithms to network-like graphs (small-world structures, grid networks).
 
2.	Progressive Examples:
 - Example 1: Simple undirected graph (3-4 nodes).
 - Example 2: Directed graph (5-6 nodes).
 - Example 3: Network structure (like a grid or small-world).

3.	Final Demonstration:
 - Input parsing from stdin or file (matching the C assignment format).
 - Full BFS and DFS traversal with output formatting:
 - BFS shows distances.
 - DFS shows finish times.
