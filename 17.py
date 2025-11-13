# Global variable for simplicity
graph = {}

def create_graph():
    global graph
    graph = {}
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        graph[i] = []

    e = int(input("Enter number of edges: "))
    for i in range(e):
        u = int(input(f"Enter source node of edge {i+1}: "))
        v = int(input(f"Enter destination node of edge {i+1}: "))
        graph[u].append(v)
        graph[v].append(u)  # undirected graph
    print("Graph created successfully!")


def display():
    global graph
    if not graph:
        print("Graph not created yet!")
        return
    print("\nAdjacency List of Graph:")
    for node in graph:
        print(node, "->", graph[node])
    print()


def bfs():
    global graph
    if not graph:
        print("Graph not created yet!")
        return
    start = int(input("Enter starting node for BFS: "))

    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()


# ---------------- MAIN PROGRAM ----------------
def menu():
    print("""
===== MENU =====
1) Create Graph
2) Display Graph
3) BFS Traversal
4) Exit
================
""")


while True:
    menu()
    ch = int(input("Enter your choice: "))

    if ch == 1:
        create_graph()
    elif ch == 2:
        display()
    elif ch == 3:
        bfs()
    elif ch == 4:
        print("THANK YOU!!!")
        break
    else:
        print("Invalid choice! Please enter 1–4.")

