# ----------- EXPRESSION TREE USING PREFIX -----------

tree = None  # Global tree


def is_operator(ch):
    return ch in ['+', '-', '*', '/', '^']


def create_tree():
    global tree
    prefix = input("Enter prefix expression: ")
    stack = []
    for ch in prefix[::-1]:
        if not is_operator(ch):
            stack.append([ch, None, None])  # node = [data, left, right]
        else:
            left = stack.pop()
            right = stack.pop()
            stack.append([ch, left, right])
    tree = stack[0]
    print("Expression Tree created successfully!")


def postorder():
    if tree is None:
        print("Tree not created yet! Please create first.")
        return
    print("Postorder Traversal:", end=" ")
    postorder_traversal(tree)
    print()


def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node[1])
        postorder_traversal(node[2])
        print(node[0], end=" ")


def delete_tree():
    global tree
    if tree is None:
        print("Tree not created yet!")
        return
    delete_nodes(tree)
    tree = None
    print("Tree deleted successfully.")


def delete_nodes(node):
    if node is not None:
        delete_nodes(node[1])
        delete_nodes(node[2])
        node[0] = None


def menu():
    print("""
========== MENU ==========
1) Create Expression Tree
2) Postorder Traversal
3) Delete Tree
4) Exit
==========================
""")


# ------------------ MAIN PROGRAM ------------------
while True:
    menu()
    ch = int(input("Enter your choice: "))

    if ch == 1:
        create_tree()
    elif ch == 2:
        postorder()
    elif ch == 3:
        delete_tree()
    elif ch == 4:
        print("THANK YOU!!!")
        break
    else:
        print("Invalid choice! Please enter 1–4.")
