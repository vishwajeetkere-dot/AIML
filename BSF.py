from collections import deque

# Graph representation using an Adjacency List
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "F": ["I", "J"],
}


def bfs(graph, start_node):
    """Performs Breadth-First Search (BFS) starting from start_node."""
    visited = set()  # Using a set for O(1) lookups
    queue = deque([start_node])  # Using deque for O(1) pop operations

    visited.add(start_node)

    print("Following is the Breadth-First Search:")

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()  # For a clean newline at the end


if __name__ == "__main__":
    bfs(graph, "A")