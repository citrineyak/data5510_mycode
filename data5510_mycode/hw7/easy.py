class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_value(root, value):

    if root is None:

        return Node(value)

    if value < root.value:
        # I asked ChatGPT how do I get it to go again and it showed me how to do this.
        root.left = insert_value(root.left, value)

    elif value > root.value:
        root.right = insert_value(root.right, value)

    return root

root = Node(10)
print(insert_value(root, 5))
insert_value(root, 15)