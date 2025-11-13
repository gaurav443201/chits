def is_operator(ch):
    return ch in ['+', '-', '*', '/', '^']


def create_tree(prefix):
    stack = []
    for ch in prefix[::-1]:
        if not is_operator(ch):
            stack.append([ch, None, None])   # node = [data, left, right]
        else:
            left = stack.pop()
            right = stack.pop()
            stack.append([ch, left, right])
    print("Expression Tree created successfully!")
    return stack[0]


def postorder(node):
    if node is not None:
        postorder(node[1])
        postorder(node[2])
        print(node[0], end=" ")


def delete_tree(node):
    if node is not None:
        delete_tree(node[1])
        delete_tree(node[2])
        node[0] = None


# ------------------ MAIN PROGRAM ------------------
tree = None

while True:
    print("""
========== MENU ==========
1) Create Expression Tree
2) Postorder Traversal
3) Delete Tree
4) Exit
==========================
""")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        prefix = input("Enter prefix expression: ")
        tree = create_tree(prefix)

    elif ch == 2:
        if tree is None:
            print("Tree not created yet! Please create first.")
        else:
            print("\nPostorder Traversal:")
            postorder(tree)
            print()

    elif ch == 3:
        if tree is None:
            print("Tree not created yet!")
        else:
            delete_tree(tree)
            tree = None
            print("Tree deleted successfully.")

    elif ch == 4:
        print("THANK YOU!!!")
        break

    else:
        print("Invalid choice! Please enter 1–4.")
