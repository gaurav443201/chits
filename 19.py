def insert(root, key):
    if root is None:
        return [key, None, None]  # [data, left, right]

    if key < root[0]:
        root[1] = insert(root[1], key)
    elif key > root[0]:
        root[2] = insert(root[2], key)
    else:
        print("Duplicate key not allowed!")
    return root

def search(root, key):
    if root is None:
        print("Key not found.")
        return
    if key == root[0]:
        print("Key found:", key)
    elif key < root[0]:
        search(root[1], key)
    else:
        search(root[2], key)

def inorder(root):
    if root is not None:
        inorder(root[1])
        print(root[0], end=" ")
        inorder(root[2])

# ------------------------------------
root = None

while True:
    print("""
Menu:
1) Insert
2) Search
3) Display (Inorder)
4) Exit
""")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        key = int(input("Enter key to insert: "))
        root = insert(root, key)
    elif ch == 2:
        key = int(input("Enter key to search: "))
        search(root, key)
    elif ch == 3:
        print("Inorder Traversal:", end=" ")
        inorder(root)
        print()
    elif ch == 4:
        break
    else:
        print("Invalid choice!")
