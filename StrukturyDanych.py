# imports
import random

# helper functions
def printArray(arr):
    for i in range(len(arr)):
        print(i,": ",arr[i])

# sort function
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def callMergeSort(arr):
    mergeSort(arr,0,len(arr)-1)
    arr.reverse()

# data input
num_of_arrays = 15
n = 5
tree_collection = []
for i in range(num_of_arrays):
    arr = []
    for j in range(n):
        rng = random.randint(10,10000)
        arr += [rng]
    callMergeSort(arr)
    tree_collection += [arr]
    n+=5

# text printing contents of arrays
# for i in range(num_of_arrays):
#     printArray(tree_collection[i])


# Binary tree search
class BTS:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# insertion int bts
def insert(root, key):
    if root is None:
        return BTS(key)
    if root.val == key:
            return root
    if root.val < key:
            root.right = insert(root.right, key)
    else:
            root.left = insert(root.left, key)
    return root

# pirinting BTS in order
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# function to search a key in a BST
def search(root, key):
  
    # Base Cases: root is null or key 
    # is present at root
    if root is None or root.val == key:
        return root
    
    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)
    
    # Key is smaller than root's key
    return search(root.left, key)

# finds the smallest element of the tree
def findMin(root):
    if root.left is None:
        print(root.val)
    else:
        print(root.val, end=" ")
        findMin(root.left)

# finds the largest element of the tree
def findMax(root):
    if root.right is None:
        print(root.val)
    else:
        print(root.val,end=" ")
        findMax(root.right)

# helper function for node deltion
def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

# node delition
def del_node(root, x):
    if root is None:
        return root

    # If key to be searched is in a subtree
    if root.val > x:
        root.left = del_node(root.left, x)
    elif root.val < x:
        root.right = del_node(root.right, x)
    else:
        # If root matches with the given key

        # Cases when root has 0 children or only right child
        if root.left is None:
            return root.right

        # When root has only left child
        if root.right is None:
            return root.left

        # When both children are present
        succ = get_successor(root)
        root.val = succ.val
        root.right = del_node(root.right, succ.val)
        
    return root

def delete_node(root):
    print("How many nodes to delete?")
    n = int(input())
    for i in range(n):
        print("delete node with key: ")
        key = int(input())
        del_node(root,key)

def preOrder(node):
    if not node:
        return

    # Visit the current node first
    # res.append(node.val)
    print(node.val, end=" ")

    # Traverse the left subtree
    preOrder(node.left)

    # Traverse the right subtree
    preOrder(node.right)

def postOrder(node, res):
    if node is None:
        return

    # First we traverse left subtree
    postOrder(node.left, res)

    # After visiting left, traverse right subtree
    postOrder(node.right, res)

    # now we visit node
    res.append(node.val)

def drop_tree(node):
    if node is None:
        return

    # First we traverse left subtree
    drop_tree(node.left)

    # After visiting left, traverse right subtree
    drop_tree(node.right)

    print(node.val, end=" ")
    node.val = None
    node.left = None
    node.right = None


def pre_order_search(root):
    print("Enter the key of the sub tree you want to search: ")
    key = int(input())
    sub_root = search(root, key)
    preOrder(sub_root)

