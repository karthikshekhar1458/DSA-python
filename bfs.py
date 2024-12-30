from collections import deque, defaultdict

def bfs(graph, start):
    # Initialize the queue and visited set
    queue = deque([start])
    visited = set([start])
    
    while queue:
        # Dequeue a vertex from queue
        node = queue.popleft()
        print(node, end=" ")
        
        # Explore neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def add_edge(graph, u, v):
    """Helper function to add an edge to the graph (undirected)."""
    graph[u].append(v)
    graph[v].append(u)

def create_graph(edges):
    """Function to create a graph from a list of edges."""
    graph = defaultdict(list)  # Automatically initializes lists for missing keys
    for u, v in edges:
        add_edge(graph, u, v)
    return graph

# Example usage
if __name__ == "__main__":
    # List of edges for an undirected graph
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4)]
    
    # Create graph from edges
    graph = create_graph(edges)
    
    # Define start node for BFS
    start_node = 0
    print(f"BFS traversal starting from node {start_node}:")
    bfs(graph, start_node)
