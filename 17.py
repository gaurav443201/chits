def create_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        graph[i] = []

    e = int(input("Enter number of edges: "))
    for i in range(e):
        u = int(input(f"Enter source node of edge {i+1}: "))
        v = int(input(f"Enter destination node of edge {i+1}: "))
        graph[u].append(v)
        graph[v].append(u)  # for undirected graph
    print("Graph created successfully!")
    return graph


def display(graph):
    print("\nAdjacency List of Graph:")
    for node in graph:
        print(node, "->", graph[node])
    print()


def bfs(graph, start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    print("BFS Traversal:", end=" ")
    while len(queue) > 0:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()


# ---------------- MAIN PROGRAM ----------------
graph = {}

while True:
    print("""
===== MENU =====
1) Create Graph
2) Display Graph
3) BFS Traversal
4) Exit
================
""")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        graph = create_graph()

    elif ch == 2:
        if len(graph) == 0:
            print("Graph is empty! Please create a graph first.")
        else:
            display(graph)

    elif ch == 3:
        if len(graph) == 0:
            print("Graph is empty! Please create a graph first.")
        else:
            start = int(input("Enter starting node for BFS: "))
            if start in graph:
                bfs(graph, start)
            else:
                print("Invalid starting node!")

    elif ch == 4:
        print("THANK YOU!!!")
        break

    else:
        print("Invalid choice! Please enter 1–4.")
