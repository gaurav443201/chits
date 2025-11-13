def create_graph():
    n = int(input("Enter number of nodes: "))

    # create n x n adjacency matrix filled with 0
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)

    e = int(input("Enter number of edges: "))
    for i in range(e):
        u = int(input(f"Enter source node of edge {i+1}: "))
        v = int(input(f"Enter destination node of edge {i+1}: "))
        matrix[u][v] = 1
        matrix[v][u] = 1   # undirected graph

    print("Graph created successfully!")
    return matrix, n


def display(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)
    print()


def dfs(matrix, start, visited):
    print(start, end=" ")
    visited[start] = 1
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and visited[i] == 0:
            dfs(matrix, i, visited)


# ----------------------- MAIN PROGRAM -----------------------
matrix = []
n = 0

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
        matrix, n = create_graph()

    elif ch == 2:
        if len(matrix) == 0:
            print("Graph is empty! Please create a graph first.")
        else:
            display(matrix)

    elif ch == 3:
        if len(matrix) == 0:
            print("Graph is empty! Please create a graph first.")
        else:
            start = int(input("Enter starting node for DFS: "))
            if start < n:
                visited = [0] * n
                print("DFS Traversal:", end=" ")
                dfs(matrix, start, visited)
                print()
            else:
                print("Invalid starting node!")

    elif ch == 4:
        print("THANK YOU!!!")
        break

    else:
        print("Invalid choice! Please enter 1–4.")
