class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == goal:
        return path

    if start not in graph:
        return None

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path)
            if new_path:
                return new_path

    return None

if __name__ == "__main__":
    # Create the graph
    my_graph = Graph()
    my_graph.add_edge(1, 2)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(2, 4)
    my_graph.add_edge(2, 5)
    my_graph.add_edge(3, 6)
    my_graph.add_edge(3, 7)
    my_graph.add_edge(4, 8)
    my_graph.add_edge(5, 8)
    my_graph.add_edge(6, 8)
    my_graph.add_edge(7, 8)

    # Set initial and goal nodes
    initial_node = 1
    goal_node = 8

    # Find path using DFS
    result_path = dfs(my_graph.graph, initial_node, goal_node)

    # Print the result
    if result_path:
        print(f"Path from {initial_node} to {goal_node}: {result_path}")
    else:
        print(f"No path found from {initial_node} to {goal_node}")
