# ----------- Binary Search Tree (BST) -----------

root = None  # Global root node

def insert(key):
    global root
    root = insert_node(root, key)

def insert_node(node, key):
    if node is None:
        return [key, None, None]  # [data, left, right]

    if key < node[0]:
        node[1] = insert_node(node[1], key)
    elif key > node[0]:
        node[2] = insert_node(node[2], key)
    else:
        print("Duplicate key not allowed!")
    return node


def search():
    global root
    if root is None:
        print("Tree is empty!")
        return
    key = int(input("Enter key to search: "))
    search_node(root, key)

def search_node(node, key):
    if node is None:
        print("Key not found.")
        return
    if key == node[0]:
        print("Key found:", key)
    elif key < node[0]:
        search_node(node[1], key)
    else:
        search_node(node[2], key)


def inorder():
    global root
    if root is None:
        print("Tree is empty!")
        return
    print("Inorder Traversal:", end=" ")
    inorder_traversal(root)
    print()

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node[1])
        print(node[0], end=" ")
        inorder_traversal(node[2])


# ------------------ MAIN MENU ------------------
def menu():
    print("""
===== MENU =====
1) Insert
2) Search
3) Display (Inorder)
4) Exit
================
""")


while True:
    menu()
    ch = int(input("Enter your choice: "))

    if ch == 1:
        key = int(input("Enter key to insert: "))
        insert(key)
    elif ch == 2:
        search()
    elif ch == 3:
        inorder()
    elif ch == 4:
        print("THANK YOU!!!")
        break
    else:
        print("Invalid choice! Please enter 1–4.")
