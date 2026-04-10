class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Right rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Left rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Right Rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)

tree = AVLTree()
tree.insert_value(10)
tree.insert_value(20)
tree.insert_value(30)
tree.insert_value(40)
tree.insert_value(50)

print("Tree after insertion:")
# In-order traversal to print the tree
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" "),
        inorder_traversal(root.right)

def min_value(root):
    root = root.root
    while root.left:
        print(root.value, end=" ")
        root = root.left
    print(root.value)

def max_value(root):
    root = root.root
    while root.right:
        print(root.value, end=" ")
        root = root.right
    print(root.value)

def delete_node(root):
    print("How many nodes to delete?")
    n = int(input())
    for i in range(n):
        print("delete node with key: ")
        key = int(input())
        tree.delete_value(key)

def preOrder(node):
    if not node:
        return

    # Visit the current node first
    # res.append(node.val)
    print(node.value, end=" ")

    # Traverse the left subtree
    preOrder(node.left)

    # Traverse the right subtree
    preOrder(node.right)

    # to do:

    # make the droping of the tree 

    # make pre order search with key

def drop_tree(node):
    if node is None:
        return

    # First we traverse left subtree
    drop_tree(node.left)

    # After visiting left, traverse right subtree
    drop_tree(node.right)

    print(node.value, end=" ")
    node.value = None
    node.left = None
    node.right = None

def pre_order_search(root):
    print("Enter the key of the sub tree you want to search: ")
    key = int(input())
    sub_root = root.search_value(key)
    preOrder(sub_root)

inorder_traversal(tree.root)
print()

result = tree.search_value(30)
if result:
    print("Node found")
else:
    print("Node not found")

min_value(tree)
max_value(tree)
# delete_node(tree)
inorder_traversal(tree.root)
print()
preOrder(tree.root)
# print()
# drop_tree(tree.root)
# print()
# print(tree.root.value)
print()
pre_order_search(tree)