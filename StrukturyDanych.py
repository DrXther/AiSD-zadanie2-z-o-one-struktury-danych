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

for i in range(num_of_arrays):
    printArray(tree_collection[i])
    