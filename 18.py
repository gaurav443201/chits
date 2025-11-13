# Global variables
matrix = []
n = 0

def create_graph():
    global matrix, n
    n = int(input("Enter number of nodes: "))
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    e = int(input("Enter number of edges: "))
    for i in range(e):
        u = int(input(f"Enter source node of edge {i+1}: "))
        v = int(input(f"Enter destination node of edge {i+1}: "))
        matrix[u][v] = 1
        matrix[v][u] = 1   # undirected graph

    print("Graph created successfully!")


def display():
    global matrix
    if not matrix:
        print("Graph not created yet!")
        return
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)
    print()


def dfs_util(start, visited):
    global matrix
    print(start, end=" ")
    visited[start] = 1
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and visited[i] == 0:
            dfs_util(i, visited)


def dfs():
    global matrix, n
    if not matrix:
        print("Graph not created yet!")
        return
    start = int(input("Enter starting node for DFS: "))
    visited = [0] * n
    print("DFS Traversal:", end=" ")
    dfs_util(start, visited)
    print()


# ----------------------- MAIN PROGRAM -----------------------
while True:
    print("""
===== MENU =====
1) Create Graph
2) Display Graph
3) DFS Traversal
4) Exit
================
""")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        create_graph()
    elif ch == 2:
        display()
    elif ch == 3:
        dfs()
    elif ch == 4:
        print("THANK YOU!!!")
        break
    else:
        print("Invalid choice! Please enter 1–4.")
